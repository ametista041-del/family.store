import streamlit as st
from PIL import Image
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO VISUAL (ROSA E DOURADO) ---
st.markdown("""
<style>
    h1, h2, h3 { color: #EAB308 !important; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        border: none;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f2f6;
        border-radius: 10px 10px 0px 0px;
        padding: 0 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #EAB308 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO DE LIMPEZA DE LINKS ---
def preparar_video(url):
    url = url.strip()
    try:
        if "shorts/" in url:
            video_id = url.split("shorts/")[1].split("?")[0].split("&")[0]
            return f"https://www.youtube.com/watch?v={video_id}"
        if "youtu.be/" in url:
            video_id = url.split("/")[-1].split("?")[0]
            return f"https://www.youtube.com/watch?v={video_id}"
        if "watch?v=" in url:
            video_id = url.split("v=")[1].split("&")[0]
            return f"https://www.youtube.com/watch?v={video_id}"
    except:
        pass
    return url

# --- ESTADO DOS DADOS (MEMÓRIA) ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/",
        'br_desc': "O achadinho perfeito para facilitar sua rotina no Brasil!",
        'pt_desc': "A solução ideal que selecionamos para sua casa em Portugal!"
    }

# 2. PAINEL DE GESTÃO (Senha: noronha2026)
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha de Gestora:", type="password")
    if senha == "noronha2026":
        st.success("Acesso Liberado, Adriana!")
        
        with st.expander("🇧🇷 Configurar Brasil"):
            st.session_state.dados['br_vid'] = st.text_input("Link Vídeo (BR):", st.session_state.dados['br_vid'])
            st.session_state.dados['br_desc'] = st.text_area("Descrição (BR):", st.session_state.dados['br_desc'])
            st.session_state.dados['br_url'] = st.text_input("Link Loja (BR):", st.session_state.dados['br_url'])
        
        with st.expander("🇵🇹 Configurar Portugal"):
            st.session_state.dados['pt_vid'] = st.text_input("Link Vídeo (PT):", st.session_state.dados['pt_vid'])
            st.session_state.dados['pt_desc'] = st.text_area("Descrição (PT):", st.session_state.dados['pt_desc'])
            st.session_state.dados['pt_url'] = st.text_input("Link Loja (PT):", st.session_state.dados['pt_url'])
    else:
        st.info("Digite a senha para atualizar os vídeos.")

# 3. EXIBIÇÃO DO LOGO
# Tenta carregar o logo em diferentes locais possíveis
caminhos_logo = ["logo_aa.jpg", "loja_portugal/logo_aa.jpg", "logotipo A&A.jpeg"]
logo_carregado = False
for caminho in caminhos_logo:
    if os.path.exists(caminho):
        st.image(caminho, width=500)
        logo_carregado = True
        break
if not logo_carregado:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Curadoria Especial: **Adriana & Anabel**")
st.divider()

# 4. VITRINE POR ABAS
t_br, t_pt = st.tabs(["🇧🇷 Brasil", "🇵🇹 Portugal"])

def mostrar_produto(video, desc, link, label):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo")
        st.video(preparar_video(video))
    with c2:
        st.subheader("💡 Por que amamos?")
        st.write(desc)
        st.divider()
        st.link_button(label, link, use_container_width=True)

with t_br:
    mostrar_produto(st.session_state.dados['br_vid'], st.session_state.dados['br_desc'], st.session_state.dados['br_url'], "🛒 COMPRAR NO BRASIL")

with t_pt:
    mostrar_produto(st.session_state.dados['pt_vid'], st.session_state.dados['pt_desc'], st.session_state.dados['pt_url'], "🛒 COMPRAR EM PORTUGAL")

st.divider()
st.caption("© 2026 A&A Achadinhos")
