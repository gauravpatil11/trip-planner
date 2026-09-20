from trip_planner.tools.flight_tool import search_flights
from trip_planner.tools.tavily_tool import tavily_search
from backend import run_travel_agent  # type: ignore
# res = tavily_search("Best hotels in Mumbai")
# print(res)


# res = search_flights("Plan a 7 days Japan trip from Mumbai")
# print(res)

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])