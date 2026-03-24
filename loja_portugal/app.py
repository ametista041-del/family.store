import streamlit as st
from PIL import Image
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
<style>
    h1, h2, h3 { color: #EAB308; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 10px 10px 0px 0px;
        gap: 10px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #EAB308 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO PARA LIMPAR LINKS DE SHORTS ---
def preparar_video(url):
    url = url.strip()
    if "shorts/" in url:
        video_id = url.split("shorts/")[1].split("?")[0].split("&")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    if "youtu.be/" in url:
        video_id = url.split("/")[-1].split("?")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    if "watch?v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

# --- MEMÓRIA DOS PRODUTOS ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/",
        'br_desc': "O achadinho perfeito para facilitar sua rotina no Brasil!",
        'pt_desc': "A solução ideal que selecionamos para sua casa em Portugal!"
    }

# 2. PAINEL DE GESTÃO LATERAL (Senha: noronha2026)
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Digite a senha para editar:", type="password")
    if senha == "noronha2026":
        st.success("Acesso Liberado, Adriana!")
        
        st.header("🇧🇷 Configurações Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link do Vídeo (BR):", st.session_state.dados['br_vid'])
        st.session_state.dados['br_desc'] = st.text_area("Descrição (BR):", st.session_state.dados['br_desc'])
        st.session_state.dados['br_url'] = st.text_input("Link de Compra (BR):", st.session_state.dados['br_url'])
        
        st.divider()
        
        st.header("🇵🇹 Configurações Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link do Vídeo (PT):", st.session_state.dados['pt_vid'])
        st.session_state.dados['pt_desc'] = st.text_area("Descrição (PT):", st.session_state.dados['pt_desc'])
        st.session_state.dados['pt_url'] = st.text_input("Link de Compra (PT):", st.session_state.dados['pt_url'])
    else:
        st.warning("Acesse o painel para trocar os produtos.")

# 3. VITRINE PRINCIPAL
# Buscando o logo na pasta raiz (onde ele está no seu print)
arquivo_logo = "logo_aa.jpg"

if os.path.exists(arquivo_logo):
    st.image(arquivo_logo, width=600)
elif os.path.exists(f"loja_portugal/{arquivo_logo}"):
    st.image(f"loja_portugal/{arquivo_logo}", width=600)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Curadoria Especial: **Adriana & Anabel**")
st.divider()

# 4. EXIBIÇÃO POR ABAS
t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def renderizar_produto(video, descricao, link, label_botao):
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("🎬 Assista ao vídeo 👇")
        link_final = preparar_video(video)
        st.video(link_final)
    with col2:
        st.subheader("💡 Por que você precisa disso?")
        st.write(f"### {descricao}")
        st.divider()
        st.link_button(label_botao, link, use_container_width=True)

with t_br:
    renderizar_produto(
        st.session_state.dados['br_vid'], 
        st.session_state.dados['br_desc'], 
        st.session_state.dados['br_url'],
        "🛒 COMPRAR NA AMAZON BRASIL"
    )

with t_pt:
    renderizar_produto(
        st.session_state.dados['pt_vid'], 
        st.session_state.dados['pt_desc'], 
        st.session_state.dados['pt_url'],
        "🛒 COMPRAR EM PORTUGAL"
    )

st.divider()
st.caption("© 2026 A&A Achadinhos - Gerenciado por Adriana Noronha")
