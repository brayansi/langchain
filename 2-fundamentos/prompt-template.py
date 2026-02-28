from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hello, {name}!"
)

print(template.format(name="Brayan Santos"))