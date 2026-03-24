import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
import re

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO ---
st.markdown("""
<style>
    h1, h2, h3 { color: #EAB308; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO VÍDEOS ULTRA-BLINDADA ---
def preparar_video(url):
    url = url.strip()
    # Se for link de SHORTS, extrai o ID e transforma em vídeo comum
    if "shorts/" in url:
        video_id = url.split("shorts/")[1].split("?")[0].split("&")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    # Se for link curto (youtu.be)
    if "youtu.be/" in url:
        video_id = url.split("/")[-1].split("?")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    # Se for link padrão com lixo
    if "watch?v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

# --- MEMÓRIA ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/"
    }

# 2. PAINEL DE GESTÃO (Senha: noronha2026)
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha:", type="password")
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.session_state.dados['br_vid'] = st.text_input("Link Shorts/Vídeo (BR):", st.session_state.dados['br_vid'])
        loja_br = st.selectbox("Loja (BR):", ["A&A Achadinhos", "Amazon Brasil", "Shopee"], key="sbr")
        st.session_state.dados['br_url'] = st.text_input("Link Compra (BR):", st.session_state.dados['br_url'])
        st.divider()
        st.session_state.dados['pt_vid'] = st.text_input("Link Shorts/Vídeo (PT):", st.session_state.dados['pt_vid'])
        loja_pt = st.selectbox("Loja (PT):", ["A&A Achadinhos", "Amazon Espanha", "Worten"], key="spt")
        st.session_state.dados['pt_url'] = st.text_input("Link Compra (PT):", st.session_state.dados['pt_url'])
    else:
        loja_br = "A&A Achadinhos"
        loja_pt = "A&A Achadinhos"

# 3. VITRINE
arquivo_logo = "logo_aa.jpg"
if os.path.exists(arquivo_logo):
    img = Image.open(arquivo_logo)
    st.image(img, width=600)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Curadoria Especial: **Adriana & Anabel**")
st.divider()

t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar(video, loja, link):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo 👇")
        # AQUI ACONTECE A MÁGICA DA CONVERSÃO
        link_limpo = preparar_video(video)
        st.video(link_limpo)
    with c2:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### O achadinho perfeito para o seu lar.")
        st.divider()
        st.link_button(f"🛒 COMPRAR NA {loja.upper()}", link, use_container_width=True)

with t_br:
    mostrar(st.session_state.dados['br_vid'], loja_br, st.session_state.dados['br_url'])
with t_pt:
    mostrar(st.session_state.dados['pt_vid'], loja_pt, st.session_state.dados['pt_url'])

st.divider()
st.caption("© 2026 A&A Achadinhos")
