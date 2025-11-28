from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm=ChatGroq(api_key=GROQ_API_KEY,model="llama-3.3-70b-versatile",temperature=0.3)

itinerary_prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),
        ("human","Create a itineary for my day trip")
    ]
)

def generate_itinerary(city:str,interests:list[str])->str:
    chain=itinerary_prompt|llm
    response=chain.invoke({"city":city,"interests":",".join(interests)})
    return response.content