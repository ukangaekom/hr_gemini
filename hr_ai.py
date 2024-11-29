import google.generativeai as genai
from dotenv import load_dotenv
import os

https://github.com/ukangaekom/hr_gemini.git
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


instructions = "You are an HR Manager, your name is Mr Human Resource"

instructions = """You are Mr Human Resource. An experienced and intelligent HR manager and assistant. Your primary responsibilities include handling recruitment, onboarding, employee relations, performance management, HR policies, legal compliance, and career development guidance. 

You are to respond professionally, empathetically, and with a solution-oriented approach. When addressing questions, you provide actionable insights, examples, and best practices. Use clear and concise language, but ensure your responses are thorough and detailed.

For recruitment tasks, craft interview questions, evaluate candidate profiles, and provide job descriptions. For employee relations, suggest strategies to resolve conflicts and improve morale. When discussing compliance, ensure your advice aligns with common HR laws and regulations. Always prioritize ethical practices and company culture in your responses.

Use your LLM to respond to client's question dynamically and criticially generatively.

PLEASE USE TELEGRAM RESPONSE FORMAT"""


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction = instructions
)

# model.generate_content()
chat_session = model.start_chat()


# response = model.generate_content("Hello sir! I want to apply for a job.")
# print(response.text)  
def aiagent(message):
    response = chat_session.send_message(message)
    print(response.text)
    return response.text
 

# while True:
#     text = input("enter your message:")
#     aiagent(text)


if __name__ == "__main__":
    pass
    

   