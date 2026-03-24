import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- ESTILO PERSONALIZADO (Cores do seu Logo) ---
st.markdown("""
<style>
    /* Cor dos Títulos */
    h1, h2, h3 { color: #EAB308; } 
    
    /* Botão de Compra (Rosa do Logo) */
    .stLinkButton button {
        background-color: #F472B6 !important; 
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        padding: 0.8rem 1.5rem;
        border: none;
    }
    .stLinkButton button:hover {
        background-color: #EAB308 !important; /* Amarelo no hover */
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO VÍDEOS BLINDADA (Corrige Shorts e Links Sujos) ---
def formatar_link_video(url):
    url = url.strip()
    if "youtube.com/shorts/" in url:
        url = url.replace("youtube.com/shorts/", "youtube.com/watch?v=")
    if "youtube.com/watch?v=" in url:
        # Remove lixo do link como &ab_channel ou &t=
        url = url.split('&')[0]
    return url

# --- MEMÓRIA DOS DADOS ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/"
    }

# 2. PAINEL DE GESTÃO LATERAL (Senha: noronha2026)
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha de Acesso:", type="password")
    
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.divider()
        st.header("🇧🇷 Configurar Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link Vídeo (BR):", st.session_state.dados['br_vid'])
        loja_br = st.selectbox("Loja (BR):", ["A&A Achadinhos", "Amazon Brasil", "Shopee"], key="sbr")
        st.session_state.dados['br_url'] = st.text_input("Link Compra (BR):", st.session_state.dados['br_url'])
        st.divider()
        st.header("🇵🇹 Configurar Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link Vídeo (PT):", st.session_state.dados['pt_vid'])
        loja_pt = st.selectbox("Loja (PT):", ["A&A Achadinhos", "Amazon Espanha", "Worten"], key="spt")
        st.session_state.dados['pt_url'] = st.text_input("Link Compra (PT):", st.session_state.dados['pt_url'])
    else:
        loja_br = "A&A Achadinhos"
        loja_pt = "A&A Achadinhos"

# 3. VITRINE PÚBLICA (Onde o Logo aparece Grande)

# Nome do arquivo que você renomeou no GitHub
arquivo_logo = "logo_aa.jpg"

if os.path.exists(arquivo_logo):
    img = Image.open(arquivo_logo)
    # Aumentado para 600 para ficar imponente
    st.image(img, width=600)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial: **Adriana & Anabel**")
st.caption("Curadoria de mãe e filha para facilitar o seu lar. 💖")
st.divider()

t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar_produto(video, loja, link):
    col_v, col_t = st.columns([1.5, 1])
    with col_v:
        st.subheader("🎬 Assista ao vídeo 👇")
        link_final = formatar_link_video(video)
        
        if "instagram.com" in link_final:
            components.iframe(link_final.rstrip('/') + "/embed", height=500)
        else:
            st.video(link_final)
            
    with col_t:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### O achadinho perfeito para você.")
        st.write("Selecionamos essa solução para economizar seu tempo e dinheiro.")
        st.divider()
        st.link_button(f"🛒 COMPRAR NA {loja.upper()}", link, use_container_width=True)

with t_br:
    mostrar_produto(st.session_state.dados['br_vid'], loja_br, st.session_state.dados['br_url'])

with t_pt:
    mostrar_produto(st.session_state.dados['pt_vid'], loja_pt, st.session_state.dados['pt_url'])

st.divider()
st.caption("© 2026 A&A Achadinhos - Inteligência em Organização Familiar.")
