import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
import re

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO (Amarelo e Rosa) ---
st.markdown("""
<style>
    h1, h2, h3, h4 { color: #EAB308 !important; } 
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO PARA VÍDEO NO TELEMÓVEL ---
def limpar_link(url):
    url = str(url).strip()
    match = re.search(r"(?:v=|\/shorts\/|youtu\.be\/|\/embed\/)([\w-]{11})", url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    return url

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
        # AQUI VOLTAM AS CAIXINHAS DE LINK QUE SUMIRAM:
        st.header("🇧🇷 Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link Vídeo (BR):", st.session_state.dados['br_vid'])
        st.session_state.dados['br_url'] = st.text_input("Link Compra (BR):", st.session_state.dados['br_url'])
        loja_br = st.selectbox("Loja (BR):", ["A&A Achadinhos", "Amazon", "Shopee"], key="sbr")
        
        st.divider()
        st.header("🇵🇹 Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link Vídeo (PT):", st.session_state.dados['pt_vid'])
        st.session_state.dados['pt_url'] = st.text_input("Link Compra (PT):", st.session_state.dados['pt_url'])
        loja_pt = st.selectbox("Loja (PT):", ["A&A Achadinhos", "Amazon", "Worten"], key="spt")
    else:
        loja_br = loja_pt = "A&A Achadinhos"

# 3. VITRINE (LOGO CORRIGIDO)
# O nome no seu GitHub é logo_aa.jpg
nome_logo = "logo_aa.jpg" 

if os.path.exists(nome_logo):
    st.image(nome_logo, width=600)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial")
st.caption("Soluções úteis que facilitam sua rotina. 💖")
st.divider()

# --- ABAS ---
t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar(video, link, loja):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo 👇")
        v_f = limpar_link(video)
        st.markdown(f'<iframe width="100%" height="450" src="{v_f}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    with c2:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### O achadinho perfeito!")
        st.divider()
        st.link_button(f"🛒 COMPRAR NA {loja.upper()}", link, use_container_width=True)

with t_br: mostrar(st.session_state.dados['br_vid'], st.session_state.dados['br_url'], loja_br)
with t_pt: mostrar(st.session_state.dados['pt_vid'], st.session_state.dados['pt_url'], loja_pt)

st.divider()
st.caption("© 2026 A&A Achadinhos - Inteligência em Organização Familiar.")
