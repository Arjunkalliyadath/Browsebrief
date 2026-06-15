from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

with open("about_content.txt", "r", encoding="utf-8") as f:
    content = f.read()

prompt = f"""
Give me a sumary about the cmpany.

{content}
"""

response = llm.invoke(prompt)

print(response.content)