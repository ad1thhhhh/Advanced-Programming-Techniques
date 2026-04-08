import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"


response = requests.get(URL)
response.encoding = 'utf-8' 

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

book_data = []
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    rating_class = book.find("p", class_="star-rating")["class"]
    rating_word = rating_class[1]
    rating_number = rating_map[rating_word]  # convert rating to number

    book_data.append([title, rating_number, price])

csv_file = "travel_books.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Rating", "Price"])
    writer.writerows(book_data)

print(f"✅ Data saved to {csv_file}\n")

print("📄 Travel Books:\n")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
