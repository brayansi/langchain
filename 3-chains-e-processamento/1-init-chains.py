from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

template = PromptTemplate(
    input_variables=["topic"],
    template="Conte uma piada sobre {topic}"
)

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

chain = template | model

response = chain.invoke({"topic": "BTC e ETH"})

print(response.content)