import streamlit as st
import os
import re

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO VISUAL (ROSA E DOURADO) ---
st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3 { color: #EAB308 !important; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: #f8f9fa;
        border-radius: 10px 10px 0px 0px;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #EAB308 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO DE LIMPEZA DE VÍDEO (PARA SHORTS E TELEMÓVEL) ---
def ajustar_video(url):
    url = url.strip()
    # Extrai o ID do vídeo de qualquer link do YouTube
    id_match = re.search(r"(?:v=|\/shorts\/|youtu\.be\/|\/embed\/)([\w-]{11})", url)
    if id_match:
        return f"https://www.youtube.com/watch?v={id_match.group(1)}"
    return url

# --- 2. DADOS DA VITRINE (MUDA AQUI PARA MUDAR NO SITE E NO CELULAR) ---
# Substitua os links abaixo quando tiver novos produtos:
video_br = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
link_br = "https://www.amazon.com.br/"

video_pt = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
link_pt = "https://www.amazon.es/-/pt/"

# --- 3. EXIBIÇÃO DO LOGO ---
# O código tenta achar o seu logo nos nomes que vimos no GitHub
caminhos_logo = ["logo_aa.jpg", "loja_portugal/logo_aa.jpg", "logotipo A&A.jpeg"]
logo_exibido = False
for path in caminhos_logo:
    if os.path.exists(path):
        st.image(path, width=450)
        logo_exibido = True
        break

if not logo_exibido:
    st.header("🛍️ A&A Achadinhos")

st.markdown("### Curadoria Especial: **Adriana & Anabel**")
st.divider()

# --- 4. ABAS DE NAVEGAÇÃO ---
aba_br, aba_pt = st.tabs(["🇧🇷 ACHADINHOS BRASIL", "🇵🇹 ACHADINHOS PORTUGAL"])

with aba_br:
    st.subheader("🎬 Sugestão para o Brasil")
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.video(ajustar_video(video_br))
    with col2:
        st.write("#### Por que amamos este produto?")
        st.write("Item selecionado pela nossa curadoria para facilitar sua vida!")
        st.link_button("🛒 COMPRAR AGORA NO BRASIL", link_br, use_container_width=True)

with aba_pt:
    st.subheader("🎬 Sugestão para Portugal")
    col1_pt, col2_pt = st.columns([1.5, 1])
    with col1_pt:
        st.video(ajustar_video(video_pt))
    with col2_pt:
        st.write("#### Destaque em Portugal")
        st.write("A melhor opção custo-benefício que encontramos no mercado europeu!")
        st.link_button("🛒 COMPRAR AGORA EM PORTUGAL", link_pt, use_container_width=True)

st.divider()
st.caption("© 2026 A&A Achadinhos - Adriana Noronha")
