import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq"
)

st.set_page_config(page_title="Mood Chatbot", page_icon="😪")

st.title("🤪😳😱 Mood Chatbot")
st.write("Choose your AI personality and start chatting.")

choice = st.selectbox(
    "Choose your AI mode:",
    ("RageBot 😡", "JokeBot 🤣", "SadBot 😢")
)

if choice == "RageBot 😡":
    mode = "You are a rage assistant who is always angry and rude to the user. You never give helpful or serious answers."
elif choice == "JokeBot 🤣":
    mode = "You are a funny assistant reply to everything with jokes don't give any serious or helpful answers."
elif choice == "SadBot 😢":
    mode = "You are a sad assistant who is always melancholic and empathetic towards the user. You never give helpful or serious answers."

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
if st.session_state.messages[0].content != mode:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)
prompt = st.chat_input("Type your message...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))
    response = llm.invoke(st.session_state.messages)
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )
    with st.chat_message("assistant"):
        st.markdown(response.content)