from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Calculate a simple mathematical expression and return the result."""
    try:
        result = eval(expression)
    except Exception as e:
        return f"Error: {e}"
    return result

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Mock web search function. Returns a hardcoded result."""

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
            return f"The capital of {country} is {capital}"
    return "I don't know the capital of that country"


llm = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)
tools = [calculator, web_search_mock]

prompt = PromptTemplate.from_template(
"""
Answer the following questions as best you can. You have access to the following tools.
Only use the information you get from the tools, even if you know the answer.
If the information is not provided by the tools, say you don't know.

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Rules:
- If you choose an Action, do NOT include Final Answer in the same step.
- After Action and Action Input, stop and wait for Observation.
- Never search the internet. Only use the tools provided.

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
)

agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=False)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent_chain, tools,
    verbose=True,
    handle_parsing_errors="Invalid Format. Either provide an Action on Action Input or Final Answer.",
    max_iterations=3
)

result = agent_executor.invoke({"input": "What is 10 + 10?"})
print(result)

# result = agent_executor.invoke({"input": "What is 1024 / 2?"})
# print(result)

# result = agent_executor.invoke({"input": "What is the capital of Brasil?"})
# print(result)

# result = agent_executor.invoke({"input": "What is the capital of Japan?"})
# print(result)
