import streamlit as st
from PIL import Image
import os
import re

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
    }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [aria-selected="true"] { background-color: #EAB308 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO MESTRE PARA O VÍDEO (CORRIGIDA) ---
def preparar_video(url):
    url = url.strip()
    # Esta linha limpa links de Shorts e links do celular para o Streamlit aceitar
    padrao = r"(?:v=|\/shorts\/|\/embed\/|\/v\/|youtu\.be\/|\/watch\?v=|\/watch\?.+&v=)([\w-]{11})"
    resultado = re.search(padrao, url)
    if resultado:
        video_id = resultado.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    return url

# --- 2. VITRINE (TROQUE OS LINKS AQUI) ---
dados = {
    'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ", # Link do vídeo BR
    'br_url': "https://www.amazon.com.br/",                 # Link de compra BR
    'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ", # Link do vídeo PT
    'pt_url': "https://www.amazon.es/-/pt/",                # Link de compra PT
    'br_desc': "Achadinho selecionado para facilitar sua rotina no Brasil!",
    'pt_desc': "A solução ideal para sua casa em Portugal!"
}

# --- 3. EXIBIÇÃO DO LOGO ---
arquivo_logo = "logo_aa.jpg"
if os.path.exists(arquivo_logo):
    st.image(arquivo_logo, width=400)
elif os.path.exists(f"loja_portugal/{arquivo_logo}"):
    st.image(f"loja_portugal/{arquivo_logo}", width=400)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Curadoria Especial: **Adriana & Anabel**")
st.divider()

# --- 4. ABAS (BRASIL E PORTUGAL) ---
t_br, t_pt = st.tabs(["🇧🇷 Brasil", "🇵🇹 Portugal"])

def mostrar_produto(video, desc, link, label):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo")
        st.video(preparar_video(video)) # Aqui o vídeo é corrigido antes de rodar
    with c2:
        st.subheader("💡 Por que amamos?")
        st.write(desc)
        st.divider()
        st.link_button(label, link, use_container_width=True)

with t_br:
    mostrar_produto(dados['br_vid'], dados['br_desc'], dados['br_url'], "🛒 COMPRAR NO BRASIL")

with t_pt:
    mostrar_produto(dados['pt_vid'], dados['pt_desc'], dados['pt_url'], "🛒 COMPRAR EM PORTUGAL")

st.divider()
st.caption("© 2026 A&A Achadinhos")
