from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

template_to_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Traduza o texto a seguir para inglês: \n {initial_text}"
)

template_to_summarize = PromptTemplate(
    input_variables=["text"],
    template="Resuma em apenas dois nomes de comidas: {text}"
)

llm_english = ChatOpenAI(model="gpt-5-mini", temperature=0)

translate = template_to_translate | llm_english | StrOutputParser()
pipeline = {"text": translate} | template_to_summarize | llm_english | StrOutputParser()

response = pipeline.invoke({"initial_text": "Qual são as 10 comidas típicas da Espanha?"})

print(response)