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
        st.session_state.dados['br_url'] = st.text_input("Link de Compra (
