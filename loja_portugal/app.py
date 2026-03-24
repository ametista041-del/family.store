import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO DO SITE
st.set_page_config(page_title="Curadoria Adriana Noronha", layout="wide", page_icon="🏠")

# --- MEMÓRIA DE SEGURANÇA ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/"
    }

# 2. PAINEL DE GESTÃO (BARRA LATERAL)
with st.sidebar:
    st.title("⚙️ Painel de Abastecimento")
    
    # SEÇÃO BRASIL
    st.header("🇧🇷 Configurar Brasil")
    st.session_state.dados['br_vid'] = st.text_input("Link do Vídeo (BR):", st.session_state.dados['br_vid'])
    loja_br = st.selectbox("Escolha a Loja (BR):", 
                           ["Amazon Brasil", "Mercado Livre", "Shopee", "Magalu", "Outra"], key="sel_br")
    st.session_state.dados['br_url'] = st.text_input(f"Link de destino (BR):", st.session_state.dados['br_url'])

    st.divider()

    # SEÇÃO PORTUGAL
    st.header("🇵🇹 Configurar Portugal")
    st.session_state.dados['pt_vid'] = st.text_input("Link do Vídeo (PT):", st.session_state.dados['pt_vid'])
    loja_pt = st.selectbox("Escolha a Loja (PT):", 
                           ["Amazon Espanha", "IKEA Portugal", "Temu", "Worten", "Outra"], key="sel_pt")
    st.session_state.dados['pt_url'] = st.text_input(f"Link de destino (PT):", st.session_state.dados['pt_url'])

# 3. O SITE (VISÃO DO CLIENTE)
st.title("🏠 Soluções Práticas: Brasil & Portugal")
st.markdown("#### Curadoria e Gestão: **Adriana Noronha**")
st.divider()

tab_br, tab_pt = st.tabs(["🇧🇷 Loja Brasil", "🇵🇹 Loja Portugal"])

# Função que desenha a vitrine e atualiza o botão automaticamente
def desenhar_vitrine(video, nome_loja, link_loja, msg):
    col_v, col_t = st.columns([1.5, 1])
    with col_v:
        st.subheader("📺 Veja a Solução")
        if "instagram.com" in video:
            components.iframe(video.rstrip('/') + "/embed", height=500)
        else:
            st.video(video)
    with col_t:
        st.subheader("🎯 Recomendação da Adriana")
        st.write(msg)
        st.divider()
        # O NOME DO BOTÃO AGORA MUDA DE ACORDO COM O SELECTBOX
        st.link_button(f"🛒 Comprar na {nome_loja}", link_loja, use_container_width=True)

with tab_br:
    desenhar_vitrine(st.session_state.dados['br_vid'], loja_br, st.session_state.dados['br_url'], "Curadoria para sua casa no Brasil.")

with tab_pt:
    desenhar_vitrine(st.session_state.dados['pt_vid'], loja_pt, st.session_state.dados['pt_url'], "Curadoria para sua nova rotina em Portugal.")

st.divider()
st.caption("Adriana Noronha - Inteligência em Organização e Gestão.")