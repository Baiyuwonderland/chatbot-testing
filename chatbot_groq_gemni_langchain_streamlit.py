from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Chatbot", page_icon="colorful-chat-icon-futuristic-in-2050-cool-vibe-to-it.png", layout="centered")
st.title("💬 Chatbot")

with st.sidebar:
    st.header("Settings")
    model_provider = st.selectbox(
        "Select Model Provider", ["Groq (Llama)", "Google (Gemini)"]
    )
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

if model_provider == "Groq (Llama)":
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
else:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_model" not in st.session_state:
    st.session_state.current_model = model_provider

if st.session_state.current_model != model_provider:
    st.session_state.chat_history = []
    st.session_state.current_model = model_provider
    st.info(f"Switched to {model_provider}. Chat history cleared.")

st.caption(f"Using: {model_provider}")

USER_AVATAR = "a-pink-face-withe-heart-eyes-and-a-open-wide-mouth.png"
ASSISTANT_AVATAR = "2050-ai-robot-with-cool-color-futuristic.png"

for message in st.session_state.chat_history:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    avatar = USER_AVATAR if role == "user" else ASSISTANT_AVATAR
    with st.chat_message(role, avatar=avatar):
        st.markdown(message.content)

user_prompt = st.chat_input("Ask chatbot ")

if user_prompt:
    st.chat_message("user", avatar=USER_AVATAR).markdown(user_prompt)
    st.session_state.chat_history.append(HumanMessage(content=user_prompt))

    try:
        response = llm.invoke(st.session_state.chat_history)
        assistant_response = response.content
        st.session_state.chat_history.append(AIMessage(content=assistant_response))
        st.chat_message("assistant", avatar=ASSISTANT_AVATAR).markdown(
            assistant_response
        )
    except Exception as e:
        st.error(f"Error: {e}")
        st.session_state.chat_history.pop()
