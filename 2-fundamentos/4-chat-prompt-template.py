from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a an assistant that translate text in {language} language."),
    ("user", "{question}")
])

message = chat_prompt.format_messages(language="Portuguese", question="Hello, world!")

for msg in message:
    print(f"{msg.type}: {msg.content}")

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

response = model.invoke(message)

print(response.content)