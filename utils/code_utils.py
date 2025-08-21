from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Initialize LLM
llm = OllamaLLM(model="llama3:latest")

# Prompt template for code generation
code_prompt = PromptTemplate(
    input_variables=["task"],
    template="Generate Python code for the following task:\n{task}\nProvide only the code."
)

# Prompt template for explanation
explain_prompt = PromptTemplate(
    input_variables=["code"],
    template="Explain the following Python code in simple language:\n{code}"
)

def generate_code(task):
    # Correct way: pass task as a keyword argument
    return llm.invoke(code_prompt.format(task=task))

def explain_code(code):
    # Correct way: pass code as a keyword argument
    return llm.invoke(explain_prompt.format(code=code))

