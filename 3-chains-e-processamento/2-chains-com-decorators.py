from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

@chain
def squere(imput_x:dict) -> dict:
    x = imput_x["x"]
    return {"squere_result": x * x}

template = PromptTemplate(
    input_variables=["squere_result"],
    template="Tell me about the number {squere_result}"
)

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

chain = squere | template | model

response = chain.invoke({"x": 10})

print(response.content)