import requests

BASE = "https://api.openalex.org/works"

def search_openalex(query, per_page=5):
    params = {"search": query, "per-page": per_page}
    r = requests.get(BASE, params=params)
    return r.json().get("results", [])

if __name__ == "__main__":
    q = input("Search term for OpenAlex: ")
    items = search_openalex(q)
    for idx, item in enumerate(items, 1):
        title = item.get("title")
        year = item.get("publication_year")
        doi = item.get("doi")
        print(f"{idx}. {title} ({year}) DOI: {doi}")