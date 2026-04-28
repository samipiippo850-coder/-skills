import requests
from bs4 import BeautifulSoup
import csv

TARGET_URL = "https://books.toscrape.com/catalogue/category/books_1/index.html"

def fetch_books(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    books = []
    for item in soup.select(".product_pod"):
        title = item.h3.a["title"]
        books.append({"title": title})
    return books

def save_csv(data, filename="books.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} items to {filename}")

if __name__ == "__main__":
    books = fetch_books(TARGET_URL)
    save_csv(books)