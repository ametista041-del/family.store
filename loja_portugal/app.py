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

# --- FUNÇÃO PARA LIMPAR LINKS DE TELEMÓVEL/SHORTS ---
def preparar_video(url):
    url = url.strip()
    padrao = r"(?:v=|\/shorts\/|\/embed\/|\/v\/|youtu\.be\/|\/watch\?v=|\/watch\?.+&v=)([\w-]{11})"
    resultado = re.search(padrao, url)
    if resultado:
        video_id = resultado.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    return url

# --- 2. CONFIGURAÇÃO DOS PRODUTOS (VITRINE OFICIAL) ---
# Adriana, mude os links abaixo para atualizar o site e o telemóvel de uma só vez:

dados_venda = {
    'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ", # COLE O LINK DO VÍDEO BRASIL AQUI
    'br_url': "https://www.amazon.com.br/",                 # COLE O LINK DE COMPRA BRASIL AQUI
    
    'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ", # COLE O LINK DO VÍDEO PORTUGAL AQUI
    'pt_url': "https://www.amazon.es/-/pt/",                # COLE O LINK DE COMPRA PORTUGAL AQUI
    
    'br_desc': "Achadinho exclusivo para facilitar o seu dia no Brasil!",
    'pt_desc': "A solução ideal selecionada para a sua casa em Portugal!"
}

# --- 3. EXIBIÇÃO DO LOGO ---
arquivo_logo = "logo_aa.jpg"
if os.path.exists(arquivo_logo):
    st.image(arquivo_logo, width=500)
elif os.path.exists(f"loja_portugal/{arquivo_logo}"):
    st.image(f"loja_portugal/{arquivo_logo}", width=500)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Curadoria Especial: **Adriana & Anabel**")
st.divider()

# --- 4. VITRINE POR ABAS ---
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
    mostrar_produto(dados_venda['br_vid'], dados_venda['br_desc'], dados_venda['br_url'], "🛒 COMPRAR NO BRASIL")

with t_pt:
    mostrar_produto(dados_venda['pt_vid'], dados_venda['pt_desc'], dados_venda['pt_url'], "🛒 COMPRAR EM PORTUGAL")

st.divider()
st.caption("© 2026 A&A Achadinhos")
