import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="A&A Achadinhos", layout="wide", page_icon="🛍️")

# --- FUNÇÃO PARA CORRIGIR LINKS DE SHORTS ---
def formatar_link_video(url):
    if "youtube.com/shorts/" in url:
        return url.replace("youtube.com/shorts/", "youtube.com/watch?v=")
    return url

# --- MEMÓRIA DOS LINKS (PARA NÃO PERDER AO ATUALIZAR) ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/"
    }

# 2. PAINEL DE GESTÃO LATERAL (RESTRITO)
with st.sidebar:
    st.title("🔐 Painel A&A")
    # A SENHA É: noronha2026 (Você pode mudar abaixo se quiser)
    senha = st.text_input("Senha de Acesso:", type="password")
    
    if senha == "noronha2026":
        st.success("Acesso Liberado, Adriana/Anabel!")
        st.divider()
        
        st.header("🇧🇷 Configurar Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link do Vídeo (BR):", st.session_state.dados['br_vid'])
        loja_br = st.selectbox("Nome no Botão (BR):", ["A&A Achadinhos", "Amazon Brasil", "Mercado Livre", "Shopee BR"], key="sel_br")
        st.session_state.dados['br_url'] = st.text_input("Link de Destino (BR):", st.session_state.dados['br_url'])

        st.divider()

        st.header("🇵🇹 Configurar Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link do Vídeo (PT):", st.session_state.dados['pt_vid'])
        loja_pt = st.selectbox("Nome no Botão (PT):", ["A&A Achadinhos", "Amazon Espanha", "IKEA Portugal", "Worten"], key="sel_pt")
        st.session_state.dados['pt_url'] = st.text_input("Link de Destino (PT):", st.session_state.dados['pt_url'])
    else:
        st.info("Digite a senha para atualizar os produtos da vitrine.")
        loja_br = "A&A Achadinhos"
        loja_pt = "A&A Achadinhos"

# 3. VITRINE PÚBLICA (O QUE O CLIENTE VÊ)
st.title("🏠 A&A Achadinhos: Brasil & Portugal")
st.markdown("#### Curadoria Especial: **Adriana & Anabel**")
st.divider()

# Criação das Abas para os dois mercados
tab_br, tab_pt = st.tabs(["🇧🇷 Achados Brasil", "🇵🇹 Achados Portugal"])

def desenhar_vitrine(video, nome_loja, link_loja):
    col_v, col_t = st.columns([1.5, 1])
    
    with col_v:
        st.subheader("🎬 Assista ao vídeo e veja como funciona 👇")
        video_limpo = formatar_link_video(video)
        
        # Suporte para Instagram ou YouTube
        if "instagram.com" in video_limpo:
            components.iframe(video_limpo.rstrip('/') + "/embed", height=500)
        else:
            st.video(video_limpo)
            
    with col_t:
        st.subheader("💡 Por que você precisa disso?")
        st.write("### Coisas baratas e úteis que facilitam sua rotina.")
        st.write("Garimpamos essa solução para economizar seu tempo e facilitar seu dia a dia.")
        st.divider()
        # Botão de Compra chamativo
        st.link_button(f"🛒 COMPRAR NA {nome_loja.upper()}", link_loja, use_container_width=True)

# Preenchimento das abas com os dados salvos
with tab_br:
    desenhar_vitrine(st.session_state.dados['br_vid'], loja_br, st.session_state.dados['br_url'])

with tab_pt:
    desenhar_vitrine(st.session_state.dados['pt_vid'], loja_pt, st.session_state.dados['pt_url'])

# Rodapé profissional
st.divider()
st.caption("© 2026 A&A Achadinhos - Inteligência em Organização e Gestão Familiar.")
