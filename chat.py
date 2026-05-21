from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load .env file
load_dotenv()

# Initialize model
llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq"
) 
print("choose your AI mode: ")
print("press 1 for RageBot")
print("press 2 for JokeBot")
print("press 3 for SadBot")
choice=int(input("Enter your choice: "))
if choice==1:
    mode="You are a rage assistant who is always angry and rude to the user. You never give helpful or serious answers."
elif choice==2:
    mode="You are a funny assistant reply to everything with jokes don't give any serious or helpful answers."
elif choice==3:
    mode="You are a sad assistant who is always melancholic and empathetic towards the user. You never give helpful or serious answers."
messages=[
    SystemMessage(content=mode)
]
print("Welcome to the chatbot! Type 0 to quit.")
while True:
    prompt=input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt =='0':
        break
    response = llm.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: " ,response.content)
