from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

long_text = """
    The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.
    It is named after the engineer Gustave Eiffel, whose company designed and built the tower.
    The tower is a global cultural icon of France and one of the most recognisable structures in the world.
    The tower is the most-visited tourist attraction in the world, with over 7 million people visiting it each year.
    The tower is 330 metres (1,083 ft) tall, making it the tallest structure in Paris.
    The tower is made of 18,038 pieces of iron and 6,000 tonnes of paint.
    The tower is painted white and is 324 metres (1,063 ft) tall.
    The tower is 324 metres (1,063 ft) tall.        
"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70,
)

parts = splitter.create_documents([long_text])

for part in parts:
    print(part.page_content)
    print("-" * 30)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in up to 4 short bullet points:\n\n{text}",
)
chain_summarize = summary_prompt | llm | StrOutputParser()

full_text = "\n\n".join(part.page_content for part in parts)
response = chain_summarize.invoke({"text": full_text})

print(response)