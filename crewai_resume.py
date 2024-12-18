from crew import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="",
                             verbose = True,
                             temperature=0.5,
                             google_api_key=os.getenv("GEMINI_API_KEY"))






#Agents 

resume_consultant = Agent()


career_coach = Agent()

talent_acquisition_agent = Agent()  




#Task


#Crew