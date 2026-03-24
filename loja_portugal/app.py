import streamlit as st
import os
import re

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO VISUAL (AMARELO E ROSA) ---
st.markdown("""
<style>
    h1, h2, h3, h4 { color: #EAB308 !important; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [aria-selected="true"] { background-color: #EAB308 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO DE VÍDEO ---
def ajustar_video(url):
    url = str(url).strip()
    id_match = re.search(r"(?:v=|\/shorts\/|youtu\.be\/|\/embed\/)([\w-]{11})", url)
    if id_match:
        return f"https://www.youtube.com/watch?v={id_match.group(1)}"
    return url

# --- LER CONFIGURAÇÕES (OU USAR PADRÃO SE ESTIVER VAZIO) ---
# Aqui garantimos que as abas nunca sumam!
v_br = st.secrets.get("video_br", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
l_br = st.secrets.get("link_br", "https://www.amazon.com.br/")
v_pt = st.secrets.get("video_pt", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
l_pt = st.secrets.get("link_pt", "https://www.amazon.es/-/pt/")

# --- LOGO ---
nome_logo = "logotipo A&A.jpeg"
if os.path.exists(nome_logo):
    st.image(nome_logo, width=350)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial: **Adriana & Anabel**")
st.divider()

# --- 4. AS ABAS (AQUI ELAS ESTÃO!) ---
tab_br, tab_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

with tab_br:
    st.subheader("🎬 Sugestão para o Brasil")
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.video(ajustar_video(v_br))
    with c2:
        st.write("### O achadinho perfeito!")
        st.link_button("🛒 COMPRAR NO BRASIL", l_br, use_container_width=True)

with tab_pt:
    st.subheader("🎬 Sugestão para Portugal")
    c1p, c2p = st.columns([1.5, 1])
    with c1p:
        st.video(ajustar_video(v_pt))
    with c2p:
        st.write("### Destaque em Portugal")
        st.link_button("🛒 COMPRAR EM PORTUGAL", l_pt, use_container_width=True)

st.divider()
st.caption("© 2026 A&A Achadinhos - Adriana Noronha")
