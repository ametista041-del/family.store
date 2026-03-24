import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="Curadoria Adriana Noronha", layout="wide", page_icon="🏠")

# --- FUNÇÃO PARA CORRIGIR SHORTS ---
def formatar_link_video(url):
    if "youtube.com/shorts/" in url:
        return url.replace("youtube.com/shorts/", "youtube.com/watch?v=")
    return url

# --- MEMÓRIA DOS LINKS ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'br_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'pt_vid': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'br_url': "https://www.amazon.com.br/",
        'pt_url': "https://www.amazon.es/-/pt/"
    }

# 2. PAINEL DE GESTÃO (COM SENHA)
with st.sidebar:
    st.title("🔐 Área Administrativa")
    senha = st.text_input("Digite a senha para editar:", type="password")
    
    # A SENHA QUE ESCOLHI É: noronha2026
    if senha == "noronha2026":
        st.success("Acesso Liberado!")
        st.divider()
        
        st.header("🇧🇷 Configurar Brasil")
        st.session_state.dados['br_vid'] = st.text_input("Link do Vídeo (BR):", st.session_state.dados['br_vid'])
        loja_br = st.selectbox("Loja (BR):", ["Loja Family", "Loja Noronha", "Amazon Brasil", "Outra"], key="sel_br")
        st.session_state.dados['br_url'] = st.text_input("Link de destino (BR):", st.session_state.dados['br_url'])

        st.divider()

        st.header("🇵🇹 Configurar Portugal")
        st.session_state.dados['pt_vid'] = st.text_input("Link do Vídeo (PT):", st.session_state.dados['pt_vid'])
        loja_pt = st.selectbox("Loja (PT):", ["Loja Family", "Loja Noronha", "Amazon Espanha", "Outra"], key="sel_pt")
        st.session_state.dados['pt_url'] = st.text_input("Link de destino (PT):", st.session_state.dados['pt_url'])
    else:
        st.warning("Aguardando senha para liberar edição...")
        # Valores padrão caso ninguém mude nada
        loja_br = "Amazon Brasil"
        loja_pt = "Amazon Espanha"

# 3. VITRINE (O QUE O CLIENTE VÊ)
st.title("🏠 Soluções Práticas: Brasil & Portugal")
st.markdown("#### Curadoria e Gestão: **Adriana Noronha**")
st.divider()

tab_br, tab_pt = st.tabs(["🇧🇷 Loja Brasil", "🇵🇹 Loja Portugal"])

def desenhar_vitrine(video, nome_loja, link_loja, msg):
    col_v, col_t = st.columns([1.5, 1])
    with col_v:
        st.subheader("📺 Veja a Solução")
        video_limpo = formatar_link_video(video)
        if "instagram.com" in video_limpo:
            components.iframe(video_limpo.rstrip('/') + "/embed", height=500)
        else:
            st.video(video_limpo)
    with col_t:
        st.subheader("🎯 Recomendação da Adriana")
        st.write(msg)
        st.divider()
        st.link_button(f"🛒 Ir para a {nome_loja}", link_loja, use_container_width=True)

with tab_br:
    desenhar_vitrine(st.session_state.dados['br_vid'], loja_br, st.session_state.dados['br_url'], "Curadoria para sua casa no Brasil.")

with tab_pt:
    desenhar_vitrine(st.session_state.dados['pt_vid'], loja_pt, st.session_state.dados['pt_url'], "Curadoria para sua nova rotina em Portugal.")
