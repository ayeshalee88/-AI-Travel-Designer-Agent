AI Travel Designer Agent
🧠 What It Does
The AI Travel Designer Agent helps plan a complete travel experience by coordinating between multiple specialized AI agents. It can suggest destinations based on your mood or interests, recommend flights, and even help you find suitable hotels. It also guides you to explore attractions, food spots, and activities in your chosen destination.

To achieve this, it uses two main tools – get_flights() for flight information and suggest_hotels() for hotel recommendations. Both tools work with mock data for demonstration purposes.

🔄 How It Works
This agent system uses a handoff mechanism to route your queries to the right specialist agent:

DestinationAgent → Suggests new places to travel based on your preferences.

BookingAgent → Helps simulate travel bookings like flights and hotels.

ExploreAgent → Suggests tourist attractions, local activities, and food options.

The main agent listens to your query and decides which specialized agent should handle it, ensuring smooth routing between destination discovery, booking, and exploration.

⚙️ Tech & Tools
This setup uses the OpenAI Agent SDK along with the Runner to manage agent execution. The tools include a Travel Info Generator for flight mock data and a Hotel Picker for simple hotel suggestions. The system demonstrates how agents can collaborate by handoffing user queries seamlessly between Destination, Booking, and Explore Agents.