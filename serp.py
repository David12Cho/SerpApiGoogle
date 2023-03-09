from serpapi import GoogleSearch
def google_search():
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

google_search();

