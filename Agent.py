from langchain_ollama import OllamaLLM
model = OllamaLLM(model = "llama3.2")
answer = model.invoke(input = "hello World")
print(answer)