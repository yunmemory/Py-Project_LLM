import requests
from bs4 import BeautifulSoup

url = 'https://www.niche.com/k12/marshall-high-school-falls-church-va/reviews/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
reviews = []

for review in soup.find_all('div', {'class': 'overflow-text__content'}):
    # Replace 'div' and 'class' with the actual HTML tag and class that wraps each review.
    reviews.append(review.text)

print(reviews)
