import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
import re

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
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO VÍDEOS ---
def formatar_link_video(url):
    url = str(url).strip()
    if "youtube.com/shorts/" in url:
        return url.replace("youtube.com/shorts/", "youtube.com/watch?v=")
    return url

# --- NOVA MEMÓRIA (Lê do Secrets para não esquecer no telemóvel) ---
# Se não houver nada no Secrets, ele usa esses links de reserva:
v_br_padrao = st.secrets.get("video_br", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
l_br_padrao = st.secrets.get("link_br", "https://www.amazon.com.br/")
v_pt_padrao = st.secrets.get("video_pt", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
l_pt_padrao = st.secrets.get("link_pt", "https://www.amazon.es/-/pt/")

# 2. PAINEL DE GESTÃO (Senha: noronha2026)
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha de Acesso:", type="password")
    
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.info("Para mudar o vídeo de vez no telemóvel, cole os links no menu 'Settings > Secrets' do seu painel Streamlit.")
        loja_br = st.selectbox("Loja (BR):", ["A&A Achadinhos", "Amazon Brasil", "Shopee"], key="sbr")
        loja_pt = st.selectbox("Loja (PT):", ["A&A Achadinhos", "Amazon Espanha", "Worten"], key="spt")
    else:
        loja_br = "A&A Achadinhos"
        loja_pt = "A&A Achadinhos"

# 3. VITRINE PÚBLICA
nome_logo = "logotipo A&A.jpeg"
if os.path.exists(nome_logo):
    st.image(Image.open(nome_logo), width=350)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial: **Adriana & Anabel**")
st.divider()

t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar_produto(video, loja, link):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo 👇")
        v = formatar_link_video(video)
        st.video(v)
    with c2:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### O achadinho perfeito para o seu lar.")
        st.divider()
        st.link_button(f"🛒 COMPRAR NA {loja.upper()}", link, use_container_width=True)

with t_br:
    mostrar_produto(v_br_padrao, loja_br, l_br_padrao)
with t_pt:
    mostrar_produto(v_pt_padrao, loja_pt, l_pt_padrao)

st.divider()
st.caption("© 2026 A&A Achadinhos - Adriana Noronha")
