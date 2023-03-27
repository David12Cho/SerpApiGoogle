from serpapi import GoogleSearch
import os
import pprint
import json
def google_search_map():
    #parameters include google maps and coffee
    params = {
        "engine": "google_maps",
        "q": "coffee",
        "google_domain": "google.com",
        "type": "search",
        "ll": "@40.7455096,-74.0083012,14z",
    }
    #initate google search
    searcher = GoogleSearch(params)
    #converts to dict
    data = searcher.get_dict()

    print("Local results")

    #iterates through local results in google
    for result in data['local_results']:
      print(f"""Title: {result['title']}
    Address: {result['address']}
    Rating: {result['rating']}
    Reviews: {result['reviews']}
""")
def search(num, query):
    api_key = os.getenv("80eb092cedc9d3d512f5d9c7abfeb5bd7f54a48827131f4cebd71c235ec8982f")

    params = {
        "api_key": "80eb092cedc9d3d512f5d9c7abfeb5bd7f54a48827131f4cebd71c235ec8982f",
        "engine": "google",
        "q": query,
        "num": num,
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    if "organic_results" in results:
        print("Top search results:")
        for index, result in enumerate(results["organic_results"], start=1):
            print(f"{index}. {result['title']}")
            print(f"   {result['link']}")
    else:
        print("No search results found.")

query = input("Enter your search query: ")
results = input("Please enter the number of results you would like: ")
search(results, query)
