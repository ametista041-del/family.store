import streamlit as st
import streamlit.components.v1 as components
import os
import time

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
<style>
    h1, h2, h3, h4 { color: #EAB308; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
    }
    .stLinkButton button:hover {
        background-color: #EAB308 !important;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO VÍDEOS ---
def formatar_link_video(url):
    if "youtube.com/shorts/" in url:
        return url.replace("youtube.com/shorts/", "youtube.com/watch?v=")
    return url

def gerar_iframe_video(url):
    refresh_token = str(int(time.time()))
    if "instagram.com" in url:
        return url.rstrip('/') + "/embed?refresh=" + refresh_token
    elif "youtube.com/watch?v=" in url:
        return url.replace("watch?v=", "embed/") + "?refresh=" + refresh_token
    else:
        return None

# --- MEMÓRIA ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/"
    }

# 2. PAINEL DE GESTÃO
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha de Acesso:", type="password")
    
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.divider()
        st.header("🇧🇷 Configuração Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link Vídeo (BR):", st.session_state.dados['br_vid'])
        loja_br = st.selectbox("Loja (BR):", ["A&A Achadinhos", "Amazon Brasil", "Shopee"], key="sbr")
        st.session_state.dados['br_url'] = st.text_input("Link de Compra (BR):", st.session_state.dados['br_url'])
        
        st.divider()
        
        st.header("🇵🇹 Configuração Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link Vídeo (PT):", st.session_state.dados['pt_vid'])
        loja_pt = st.selectbox("Loja (PT):", ["A&A Achadinhos", "Amazon Espanha", "Worten"], key="spt")
        st.session_state.dados['pt_url'] = st.text_input("Link de Compra (PT):", st.session_state.dados['pt_url'])
    else:
        loja_br = "A&A Achadinhos"
        loja_pt = "A&A Achadinhos"

# 3. VITRINE PÚBLICA
nome_logo = "logo_aa.jpg"  # nome correto no repositório

if os.path.exists(nome_logo):
    st.image(nome_logo, width=350)
else:
    caminho_alternativo = os.path.join("loja_portugal", nome_logo)
    if os.path.exists(caminho_alternativo):
        st.image(caminho_alternativo, width=350)
    else:
        st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial: **Adriana & Anabel**")
st.caption("Soluções baratas e úteis que facilitam sua rotina. 💖")
st.divider()

t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar_produto(video, loja, link):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo 👇")
        v =
