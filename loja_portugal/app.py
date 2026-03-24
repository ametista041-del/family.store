import streamlit as st
import pandas as pd
import os
import re

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- CONEXÃO COM A PLANILHA (O SEU ID) ---
SHEET_ID = "1xQDlup0ZRX9bWgUiuJZACL90NLKYOppTIH616_qGqsE"
URL_PLANILHA = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

# --- ESTILO VISUAL ---
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

def formatar_link_video(url):
    url = url.strip()
    id_match = re.search(r"(?:v=|\/shorts\/|youtu\.be\/|\/embed\/)([\w-]{11})", url)
    if id_match:
        return f"https://www.youtube.com/watch?v={id_match.group(1)}"
    return url

# --- CARREGAR DADOS DA PLANILHA ---
@st.cache_data(ttl=60) # Atualiza a cada 1 minuto
def carregar_dados():
    try:
        return pd.read_csv(URL_PLANILHA)
    except:
        # Se falhar, usa dados padrão
        return pd.DataFrame([["1", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://amazon.com.br", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://amazon.es"]], 
                            columns=["id", "video_br", "link_br", "video_pt", "link_pt"])

df = carregar_dados()

# --- PAINEL DE GESTÃO (SIDEBAR) ---
with st.sidebar:
    st.title("🔐 Painel A&A")
    senha = st.text_input("Senha:", type="password")
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.info("Para salvar mudanças permanentes, edite diretamente a Planilha Google.")
        st.link_button("📝 ABRIR PLANILHA AGORA", f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")

# --- EXIBIÇÃO DO LOGO ---
nome_logo = "logotipo A&A.jpeg"
if os.path.exists(nome_logo):
    st.image(nome_logo, width=350)
elif os.path.exists(f"loja_portugal/{nome_logo}"):
    st.image(f"loja_portugal/{nome_logo}", width=350)
else:
    st.title("🛍️ A&A Achadinhos")

st.markdown("#### Seleção Especial: **Adriana & Anabel**")
st.divider()

# --- ABAS ---
t_br, t_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def mostrar_produto(video, link, label):
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎬 Assista ao vídeo 👇")
        st.video(formatar_link_video(video))
    with c2:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### O achadinho perfeito para o seu lar.")
        st.divider()
        st.link_button(label, link, use_container_width=True)

# Pegando os dados da linha 1 da planilha (ou os padrões se estiver vazia)
try:
    v_br = df.iloc[0]['video_br']
    l_br = df.iloc[0]['link_br']
    v_pt = df.iloc[0]['video_pt']
    l_pt = df.iloc[0]['link_pt']
except:
    v_br = v_pt = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    l_br = "https://amazon.com.br"
    l_pt = "https://amazon.es"

with t_br:
    mostrar_produto(v_br, l_br, "🛒 COMPRAR NO BRASIL")
with t_pt:
    mostrar_produto(v_pt, l_pt, "🛒 COMPRAR EM PORTUGAL")

st.divider()
st.caption("© 2026 A&A Achadinhos")
