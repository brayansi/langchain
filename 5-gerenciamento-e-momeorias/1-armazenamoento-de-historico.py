from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

chat_model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo e sempre responde em português."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | chat_model

session_store: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

convertional_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "demo-session"}}

input_message1 = "Olá, meu nome é Brayan Santos. como você está?"
response1 = convertional_chain.invoke({"input": input_message1}, config=config)
print("humano: ", input_message1)
print("assistente: ", response1.content)
print('-' * 30)

input_message2 = "Qual é o meu nome?"
response1 = convertional_chain.invoke({"input": input_message2}, config=config)
print("humano: ", input_message2)
print("assistente: ", response1.content)
print('-' * 30)

input_message3 = "Você pode repetir meu nome em um frase motivacional?"
response1 = convertional_chain.invoke({"input": input_message3}, config=config)
print("humano: ", input_message3)
print("assistente: ", response1.content)
print('-' * 30)