from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv
load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Avalia uma expressão matemática simples e retorna o resultado como string."""
    try:
        result = eval(expression)  # cuidado: apenas para exemplo didático
    except Exception as e:
        return f"Erro: {e}"
    return str(result)

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Retorna a capital de um país, se existir nos dados mockados."""
    data = {
        "Brasil": "Brasília",
        "França": "Paris",
        "Alemanha": "Berlim",
        "Itália": "Roma",
        "Espanha": "Madri",
        "Estados Unidos": "Washington, D.C."
        
    }
    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"A capital de {country} é {capital}."
    return "Não sei a capital desse país."

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
tools = [web_search_mock]

prompt = hub.pull("hwchase17/react")
agent_chain = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain, 
    tools=tools, 
    verbose=True, 
    # max_iterations=5
)

print(agent_executor.invoke({"input": "Qual é a capital do Irã?"}))
# print(agent_executor.invoke({"input": "Quanto é 10 + 10?"}))