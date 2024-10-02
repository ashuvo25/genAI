from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

templ = """
Answer the Question.

History: {text}

Question: {question}
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(templ)

chain = prompt | model



def  genAI():
    text = ""
    print("q means exit")
    while True:
        user = input("You : ")
        if user.lower() == "q":
            break
        answer = chain.invoke({"context": text, "question": user})
        print("Roza : ",answer)
        text+= f"\nYou: {user}\nRoza: {answer}"



if __name__ == "__main__":
    genAI()


