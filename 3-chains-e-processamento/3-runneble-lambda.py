from langchain_core.runnables import RunnableLambda

def parse_number(text: str) -> int:
    return int(text.strip())

parse_number_lambda = RunnableLambda(parse_number)

number = parse_number_lambda.invoke("10")

print(f"Number: {number}", type(number))