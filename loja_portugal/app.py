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

# --- FUNÇÃO MESTRE PARA VÍDEOS (Aceita Shorts e Celular) ---
def formatar_link_video(url):
    url = url.strip()
    # Extrai o ID de 11 caracteres que o YouTube usa
    id_match = re.search(r"(?:v=|\/shorts\/|youtu\.be\/|\/embed\/)([\w-]{11})", url)
    if id_match:
        return f"https://www.youtube.com/watch?v={id_match.group(1)}"
    return url

# --- MEMÓRIA DOS VÍDEOS ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/",
        'loja_br': "Amazon Brasil",
        'loja_pt': "Amazon Espanha"
    }

# 2. PAINEL DE GESTÃO (Senha: noronha2026)
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha de Acesso:", type="password")
    
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.divider()
        st.header("🇧🇷 Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link Vídeo (BR):", st.session_state.dados['br_vid'])
        st.session_state.dados['loja_br'] = st.selectbox("Loja (BR):", ["Amazon Brasil", "Shopee", "A&A Achadinhos"])
        st.session_state.dados['br_url'] = st.text_input("Link Compra (BR):", st.session_state.dados['br_url'])
        
        st.divider()
        st.header("🇵🇹 Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link Vídeo (PT):", st.session_state.dados['pt_vid'])
        st.session_state.dados['loja_pt'] = st.selectbox("Loja (PT):", ["Amazon Espanha", "Worten", "A&A Achadinhos"])
        st.session_state.dados['pt_url'] = st.text_input("Link Compra (PT):", st.session_state.dados['pt_url'])

# 3. LOGO (Busca Automática)
nome_logo = "logotipo A&A.jpeg"
logo_caminhos = [nome_logo, f"loja_portugal/{nome_logo}", "logo_aa.jpg"]
logo_ok = False
for c in logo_caminhos:
    if os.path.exists(c):
        st.image(c, width=350)
        logo_ok = True
        break
if not logo_ok:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial: **Adriana & Anabel**")
st.divider()

# --- AS ABAS ---
t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar_produto(video, loja, link):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo 👇")
        v_limpo = formatar_link_video(video)
        st.video(v_limpo)
    with c2:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### O achadinho perfeito para o seu lar.")
        st.divider()
        st.link_button(f"🛒 COMPRAR NA {loja.upper()}", link, use_container_width=True)

with t_br:
    mostrar_produto(st.session_state.dados['br_vid'], st.session_state.dados['loja_br'], st.session_state.dados['br_url'])

with t_pt:
    mostrar_produto(st.session_state.dados['pt_vid'], st.session_state.dados['loja_pt'], st.session_state.dados['pt_url'])

st.divider()
st.caption("© 2026 A&A Achadinhos")
