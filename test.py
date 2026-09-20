from trip_planner.tools.flight_tool import search_flights
from trip_planner.tools.tavily_tool import tavily_search

res = tavily_search("Best hotels in Mumbai")
print(res)


# res = search_flights("Plan a 7 days Japan trip from Mumbai")
# print(res)