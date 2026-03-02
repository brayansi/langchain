from typing import Any


from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnableLambda

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo e sempre responde com piadas em português."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

llm = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

def prepare_inputs(payload: dict) -> dict:
    raw_history = payload.get("raw_history", [])

    trimmed_history = trim_messages(
        raw_history,
        token_counter=len,
        max_tokens=4,
        strategy="last",
        start_on = "human",
        include_system = True,
        allow_partial=False,
    )

    return {"input": payload.get("input", ""), "history": trimmed_history}

prepare_runnable = RunnableLambda[dict, dict](prepare_inputs)
chain = prepare_runnable | prompt | llm
    
session_store: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

convertional_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="raw_history"
)

config = {"configurable": {"session_id": "demo-session"}}

input_message1 = "Olá, meu nome é Brayan Santos. Não mencione meu nome."
response1 = convertional_chain.invoke({"input": input_message1}, config=config)
print("humano: ", input_message1)
print("assistente: ", response1.content)
print('-' * 30)

input_message2 = "me conte uma piada sobre Bitcoin e Ethereum. Não mencione meu nome."
response2 = convertional_chain.invoke({"input": input_message2}, config=config)
print("humano: ", input_message2)
print("assistente: ", response2.content)
print('-' * 30)

input_message3 = "Qual é o meu primeiro nome? Não mencione meu sobrenome."
response3 = convertional_chain.invoke({"input": input_message3}, config=config)
print("humano: ", input_message3)
print("assistente: ", response3.content)
print('-' * 30)

input_message4 = "Qual é o meu sobrenome?"
response4 = convertional_chain.invoke({"input": input_message4}, config=config)
print("humano: ", input_message4)
print("assistente: ", response4.content)
print('-' * 30)
