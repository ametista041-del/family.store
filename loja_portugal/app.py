import streamlit as st
import os
import re

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- FUNÇÃO DE VÍDEO ---
def ajustar_video(url):
    url = url.strip()
    id_match = re.search(r"(?:v=|\/shorts\/|youtu\.be\/|\/embed\/)([\w-]{11})", url)
    if id_match:
        return f"https://www.youtube.com/watch?v={id_match.group(1)}"
    return url

# --- LER OS LINKS DAS CONFIGURAÇÕES (SECRETS) ---
# Se não houver nada configurado, ele usa os links padrão abaixo:
v_br = st.secrets.get("video_br", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
l_br = st.secrets.get("link_br", "https://www.amazon.com.br/")
v_pt = st.secrets.get("video_pt", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
l_pt = st.secrets.get("link_pt", "https://www.amazon.es/-/pt/")

# --- ESTILO ---
st.markdown("<style>h1,h2,h3,h4{color:#EAB308!important;}.stLinkButton button{background-color:#F472B6!important;color:white!important;border-radius:12px;font-weight:bold;}</style>", unsafe_allow_html=True)

# --- LOGO ---
nome_logo = "logotipo A&A.jpeg"
if os.path.exists(nome_logo): st.image(nome_logo, width=350)
else: st.title("🛍️ A&A Achadinhos")

st.divider()

# --- ABAS ---
t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

with t_br:
    c1, c2 = st.columns([1.5, 1])
    with c1: st.video(ajustar_video(v_br))
    with c2:
        st.write("### O achadinho perfeito!")
        st.link_button("🛒 COMPRAR NO BRASIL", l_br, use_container_width=True)

with t_pt:
    c1p, c2p = st.columns([1.5, 1])
    with c1p: st.video(ajustar_video(v_pt))
    with c2p:
        st.write("### Destaque em Portugal")
        st.link_button("🛒 COMPRAR EM PORTUGAL", l_pt, use_container_width=True)
