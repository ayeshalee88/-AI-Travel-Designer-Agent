import os
from dotenv import load_dotenv
from agents import Agent,AsyncOpenAI,OpenAIChatCompletionsModel,Runner,function_tool
from agents.run import RunConfig
import asyncio

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
api_key=api_key,
base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
model="gemini-2.0-flash",
openai_client=external_client
)

config = RunConfig(
model=model,
model_provider=external_client,
tracing_disabled=True
)

@function_tool
async def get_flight(time:int,city:str)->str:
    return f"""Today PIA airline flight will depart from {city} in {time} minutes
        Today AIRSIAL airline flight will depart from {city} in {time} minutes
        Today AIRBLUE airline flight will depart from {city} in {time} minutes"""
           

@function_tool
async def get_hotel(hotelname:str,city:str)->str:
     return f"""🏨 {hotelname} Grand Hotel
            📍 Location: Sultanahmet, {city}
            ⭐ Rating: 4.5/5
            💲 Price: 120 USD per night
            ✅ Amenities: Free WiFi, Breakfast Included, Airport Shuttle

            🏨 {hotelname} Hotel
            📍 Location: Fatih, {city}
            ⭐ Rating: 4.2/5
            💲 Price: 95 USD per night
            ✅ Amenities: City View, Room Service, Spa Access"""

        
async def main():
    Destinationagent=Agent(
        name="Destination Agent",
        instructions="""You are a Destination Agent.Help user to find new places to them to travel
        Dont tell anything instead of suggesting places just excuse.DONT start reasoning on anything"""
    )

    bookingagent=Agent(
        name="Booking agent",
        instructions="""You are a Booking agent.
        -If user ask about flight booking use 'get_flight' tool
        -If user ask about Hotel booking use 'get_hotel' tool""",
        tools=[get_flight,get_hotel]
    )
    Exploreagent=Agent(
        name="Exploring Agent",
        instructions="""You are an exploring Agent.Suggest attraction and food 
        to the user in a friendly way"""
    )

    mainagent=Agent(
        name="Router Agent",
        instructions="""Your task is to receive user query and handoff to the specific agent.
        -If user ask about finding Destination handoff to 'Destinationagent'.
        -If user ask about Booking handoff to 'Bookingagent'.
        -If user ask about Exploring places handoff to 'Exploreagent
        DONT make reasoning and response by yourself""",
        handoffs=[Destinationagent,bookingagent,Exploreagent]
    )
    
    print(f"🧳 AI Travel Designer Agent")

    user=input("Ask Anything About Travel!")


    response=await Runner.run(
        mainagent,
        input=user,
        run_config=config
    )

    print(response.final_output)

if __name__=="__main__":
    asyncio.run(main())


    




