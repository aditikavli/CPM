import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


@app.route("/")
def home():
    # Get the webpage
    response = requests.get(url)

    # Check if request was successful
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Get book title
    title = soup.find("h1").text.strip()

    # Get price
    price = soup.find("p", class_="price_color").text.strip()

    # Get rating
    rating = soup.find("p", class_="star-rating")["class"][1]

    # Get number of reviews
    reviews = (
        soup.find("table", class_="table table-striped")
        .find_all("tr")[-1]
        .find("td")
        .text.strip()
    )

    # Get availability
    availability = (
        soup.find("p", class_="instock availability")
        .text
        .strip()
    )

    # Send the data to the HTML page
    return render_template(
        "book.html",
        title=title,
        price=price,
        rating=rating,
        reviews=reviews,
        availability=availability
    )


if __name__ == "__main__":
    app.run(debug=True)
    
