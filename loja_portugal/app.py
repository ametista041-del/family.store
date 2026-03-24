import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO PERSONALIZADO (Cores do seu Logo: Amarelo e Rosa) ---
st.markdown("""
<style>
    /* Cor dos Títulos */
    h1, h2, h3, h4 { color: #EAB308; } 
    
    /* Botão de Compra Personalizado */
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
    }
    .stLinkButton button:hover {
        background-color: #EAB308 !important;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO VÍDEOS ---
def formatar_link_video(url):
    if "youtube.com/shorts/" in url:
        return url.replace("youtube.com/shorts/", "youtube.com/watch?v=")
    return url

# --- MEMÓRIA ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/"
    }

# 2. PAINEL DE GESTÃO (Senha: noronha2026)
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha de Acesso:", type="password")
    
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.divider()
        st.header("🇧🇷 Configuração Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link Vídeo (BR):", st.session_state.dados['br_vid'])
        loja_br = st.selectbox("Loja (BR):", ["A&A Achadinhos", "Amazon Brasil", "Shopee"], key="sbr")
        st.session_state.dados['br_url'] = st.text_input("Link de Compra (BR):", st.session_state.dados['br_url'])
        
        st.divider()
        
        st.header("🇵🇹 Configuração Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link Vídeo (PT):", st.session_state.dados['pt_vid'])
        loja_pt = st.selectbox("Loja (PT):", ["A&A Achadinhos", "Amazon Espanha", "Worten"], key="spt")
        st.session_state.dados['pt_url'] = st.text_input("Link de Compra (PT):", st.session_state.dados['pt_url'])
    else:
        loja_br = "A&A Achadinhos"
        loja_pt = "A&A Achadinhos"

# 3. VITRINE PÚBLICA

# O SEGREDO ESTÁ AQUI: O nome tem que ser igual ao que está na raiz do seu GitHub
# Como seu arquivo está fora da pasta 'loja_portugal', usamos '../' para o código achar
nome_logo = "logotipo A&A.jpeg"

if os.path.exists(nome_logo):
    img = Image.open(nome_logo)
    st.image(img, width=350)
else:
    # Se ele não achar na raiz, tenta procurar dentro da pasta
    caminho_alternativo = os.path.join("loja_portugal", nome_logo)
    if os.path.exists(caminho_alternativo):
        img = Image.open(caminho_alternativo)
        st.image(img, width=350)
    else:
        st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial: **Adriana & Anabel**")
st.caption("Soluções baratas e úteis que facilitam sua rotina. 💖")
st.divider()

t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar_produto(video, loja, link):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo 👇")
        v = formatar_link_video(video)
        if "instagram.com" in v:
            components.iframe(v.rstrip('/') + "/embed", height=500)
        else:
            st.video(v)
    with c2:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### O achadinho perfeito para o seu lar.")
        st.write("Curadoria feita com carinho para economizar seu tempo e dinheiro.")
        st.divider()
        st.link_button(f"🛒 COMPRAR NA {loja.upper()}", link, use_container_width=True)

with t_br:
    mostrar_produto(st.session_state.dados['br_vid'], loja_br, st.session_state.dados['br_url'])
with t_pt:
    mostrar_produto(st.session_state.dados['pt_vid'], loja_pt, st.session_state.dados['pt_url'])

st.divider()
st.caption("© 2026 A&A Achadinhos - Inteligência em Organização Familiar.")
