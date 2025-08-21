from flask import Flask, render_template, request
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
import markdown
app = Flask(__name__)

# Initialize LLM
llm = OllamaLLM(model="llama3:latest")

# Prompt templates
code_prompt = PromptTemplate(
    input_variables=["task"],
    template="Generate Python code for the following task:\n{task}\nProvide only the code."
)
explain_prompt = PromptTemplate(
    input_variables=["code"],
    template="Explain the following Python code in simple language step by step:\n{code}"
)

@app.route("/", methods=["GET", "POST"])
def index():
    code = None
    explanation = None
    error = None
    task = None

    if request.method == "POST":
        action = request.form.get("action")
        task = request.form.get("task", "")
        existing_code = request.form.get("existing_code", "")

        try:
            if action == "generate_code" and task:
                code = llm.invoke(code_prompt.format(task=task))


            elif action == "explain_code" and existing_code:
                  raw_explanation = llm.invoke(explain_prompt.format(code=existing_code))
                  explanation = markdown.markdown(raw_explanation)
                  code = existing_code

            else:
                error = "Please provide input to generate or explain code."
        except Exception as e:
            error = str(e)

    return render_template("index.html", code=code, explanation=explanation, error=error, task=task)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

