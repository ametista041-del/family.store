import streamlit as st
from PIL import Image
import os
import re

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO VISUAL ---
st.markdown("""
<style>
    h1, h2, h3 { color: #EAB308 !important; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO DE LIMPEZA DE LINKS ---
def preparar_video(url):
    url = url.strip()
    padrao = r"(?:v=|\/shorts\/|\/embed\/|\/v\/|youtu\.be\/|\/watch\?v=|\/watch\?.+&v=)([\w-]{11})"
    resultado = re.search(padrao, url)
    if resultado:
        video_id = resultado.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    return url

# --- 2. VITRINE OFICIAL (Mude aqui para atualizar em todo lugar) ---
dados_venda = {
    'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
    'br_url': "https://www.amazon.com.br/",
    'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
    'pt_url': "https://www.amazon.es/-/pt/",
    'br_desc': "Achadinho exclusivo selecionado para você no Brasil!",
    'pt_desc': "A solução ideal para sua casa em Portugal!"
}

# --- 3. EXIBIÇÃO DO LOGO ---
# O código procura o seu logo_aa.jpg
if os.path.exists("logo_aa.jpg"):
    st.image("logo_aa.jpg", width=400)
elif os.path.exists("loja_portugal/logo_aa.jpg"):
    st.image("loja_portugal/logo_aa.jpg", width=400)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Curadoria Especial: **Adriana & Anabel**")
st.divider()

# --- 4. AS ABAS (BRASIL E PORTUGAL) ---
t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

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
    mostrar_produto(dados_venda['br_vid'], dados_venda['br_desc'], dados_venda['br_url'], "🛒 COMPRAR NO BRASIL")

with t_pt:
    mostrar_produto(dados_venda['pt_vid'], dados_venda['pt_desc'], dados_venda['pt_url'], "🛒 COMPRAR EM PORTUGAL")

st.divider()
st.caption("© 2026 A&A Achadinhos")
