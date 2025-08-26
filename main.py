# Import the function from the movie_search module
from movie_search import search_movies

# Define your query
my_query = 'a spy thriller in Paris'

# Get the top 3 results
results = search_movies(query=my_query, top_n=3)

# Print the results
print(f"Search results for: '{my_query}'")
print(results)