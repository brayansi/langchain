from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Calcula uma expressão matemática simples e retorna o resultado."""
    try:
        result = eval(expression)
    except Exception as e:
        return f"Erro: {e}"
    return result

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Função mock de busca na web. Retorna um resultado fixo."""

    data = {
        "Brasil": "Brasilia",
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Uruguai": "Montevideo",
        "Paraguai": "Asuncion",
        "Bolivia": "La Paz",
        "Peru": "Lima",
        "Colombia": "Bogota",
        "Venezuela": "Caracas",
        "Espanha": "Madrid",
    }

    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"A capital de {country} é {capital}"
    return "Não sei a capital desse país"


llm = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)
tools = [calculator, web_search_mock]

prompt = PromptTemplate.from_template(
"""
Responda às perguntas a seguir da melhor forma possível. Você tem acesso às seguintes ferramentas.
Use apenas as informações obtidas pelas ferramentas, mesmo que você já saiba a resposta.
Se a informação não for fornecida pelas ferramentas, diga que não sabe.

{tools}

Use o seguinte formato:

Question: a pergunta de entrada que você deve responder
Thought: você deve sempre pensar no que fazer
Action: a ação a tomar, deve ser uma entre [{tool_names}]
Action Input: a entrada para a ação
Observation: o resultado da ação

... (esse bloco Thought/Action/Action Input/Observation pode se repetir N vezes)
Thought: agora eu sei a resposta final
Final Answer: a resposta final para a pergunta original

Regras:
- Se você escolher uma Action, NÃO inclua Final Answer no mesmo passo.
- Após Action e Action Input, pare e aguarde a Observation.
- Nunca pesquise na internet. Use apenas as ferramentas fornecidas.

Comece!

Question: {input}
Thought:{agent_scratchpad}"""
)

agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=False)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent_chain, tools,
    verbose=True,
    handle_parsing_errors="Formato inválido. Forneça Action com Action Input ou Final Answer.",
    max_iterations=3
)

result = agent_executor.invoke({"input": "Quanto é 10 + 10?"})
print(result)

# result = agent_executor.invoke({"input": "Quanto é 1024 / 2?"})
# print(result)

# result = agent_executor.invoke({"input": "Qual é a capital do Brasil?"})
# print(result)

# result = agent_executor.invoke({"input": "Qual é a capital do Japão?"})
# print(result)
