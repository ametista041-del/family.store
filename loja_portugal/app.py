import streamlit as st
import re
import os

# 1. CONFIGURAÇÃO (AMARELO E ROSA)
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

st.markdown("""
<style>
    h1, h2, h3, h4 { color: #EAB308 !important; } 
    .stLinkButton button { background-color: #F472B6 !important; color: white !important; border-radius: 12px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO QUE "LIMPA" O LINK COPIADO DO TELEMÓVEL ---
def limpar_link(url):
    url = str(url).strip()
    # Pega o ID do vídeo mesmo que seja Shorts, link de partilha ou link normal
    match = re.search(r"(?:v=|\/shorts\/|youtu\.be\/|\/embed\/|youtu\.be\/)([\w-]{11})", url)
    if match:
        video_id = match.group(1)
        # Formato que o telemóvel NÃO BLOQUEIA:
        return f"https://www.youtube.com/embed/{video_id}"
    return url

# --- PAINEL LATERAL ---
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha:", type="password")
    
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        # Criamos as caixinhas onde você vai COLAR o link do telemóvel
        v_br = st.text_input("Cole o Link do Vídeo (BR):", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        l_br = st.text_input("Cole o Link da Loja (BR):", "https://amazon.com.br")
        st.divider()
        v_pt = st.text_input("Cole o Link do Vídeo (PT):", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        l_pt = st.text_input("Cole o Link da Loja (PT):", "https://amazon.es")
    else:
        v_br = v_pt = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        l_br = "https://amazon.com.br"
        l_pt = "https://amazon.es"

# --- LOGOTIPO ---
nome_logo = "logotipo A&A.jpeg"
if os.path.exists(nome_logo): st.image(nome_logo, width=300)
else: st.title("🛍️ A&A Achadinhos")

st.divider()

# --- AS ABAS ---
t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar(video, loja_link):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        link_limpo = limpar_link(video)
        # O SEGREDO: Usar Iframe para o telemóvel carregar o vídeo na hora
        st.markdown(f'<iframe width="100%" height="400" src="{link_limpo}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    with c2:
        st.write("### O achadinho perfeito!")
        st.link_button("🛒 COMPRAR AGORA", loja_link, use_container_width=True)

with t_br: mostrar(v_br, l_br)
with t_pt: mostrar(v_pt, l_pt)
