from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente que traduz textos para o idioma {language}."),
    ("user", "{question}")
])

message = chat_prompt.format_messages(language="Português", question="Olá, mundo!")

for msg in message:
    print(f"{msg.type}: {msg.content}")

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

response = model.invoke(message)

print(response.content)