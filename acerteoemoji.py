import streamlit as st
import random

st.set_page_config(page_title="🎯 Adivinhe o Emoji!", page_icon="🎮", layout="centered")

st.title("🎮 Adivinhe o Emoji!")
st.subheader("Será que você consegue decifrar todos? 😜")

# Lista de desafios
desafios = [
    {"emoji": "🏠💻", "resposta": "home office"},
    {"emoji": "🍕🎬", "resposta": "noite de filme"},
    {"emoji": "🐍💻", "resposta": "programação em python"},
    {"emoji": "🎓📚", "resposta": "estudar"},
    {"emoji": "🌍🔥", "resposta": "aquecimento global"},
    {"emoji": "🚀🌕", "resposta": "viagem espacial"},
    {"emoji": "🎧🎵", "resposta": "ouvir música"},
    {"emoji": "📸🌅", "resposta": "tirar foto do pôr do sol"},
    {"emoji": "💤😴", "resposta": "dormir"},
    {"emoji": "❤️🐶", "resposta": "amor por cachorros"},
]

# Sessão
if "pontos" not in st.session_state:
    st.session_state.pontos = 0
if "rodada" not in st.session_state:
    st.session_state.rodada = random.choice(desafios)

# Mostra o desafio
st.markdown(f"### {st.session_state.rodada['emoji']}")
resposta = st.text_input("Digite o que você acha que o emoji representa:", "")

# Botão verificar
if st.button("Verificar 🎯"):
    if resposta.lower().strip() == st.session_state.rodada["resposta"]:
        st.success("🎉 Acertou! Você é um(a) verdadeiro(a) decifrador(a) de emojis!")
        st.session_state.pontos += 1
    else:
        st.error(f"❌ Quase! A resposta era: **{st.session_state.rodada['resposta']}**")

    # Próxima rodada
    st.session_state.rodada = random.choice(desafios)

st.markdown("---")
st.markdown(f"**Pontuação atual:** {st.session_state.pontos} ⭐")

# Botão reiniciar
if st.button("🔄 Reiniciar jogo"):
    st.session_state.pontos = 0
    st.session_state.rodada = random.choice(desafios)
    st.experimental_rerun()

st.caption("Criado com 💖 e Streamlit – por você!")
