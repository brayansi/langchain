from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

template = PromptTemplate(
    input_variables=["topic"],
    template="Tell me a joke abount {topic}"
)

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

chain = template | model

response = chain.invoke({"topic": "BTC and ETH"})

print(response.content)