import requests
from bs4 import BeautifulSoup
import re
import json

# Read the categories from a JSON file
with open('categories.json', 'r') as f:
    categories = json.load(f)

# Get the website URL from user input
url = input("Enter the website URL: ")

# Define the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": url,
    "Connection": "keep-alive"
}

# Fetch the website content
res = requests.get(url, headers=headers)
html_page = res.content

# Parse the HTML content
soup = BeautifulSoup(html_page, 'html.parser')

# Extract all the text from the page
text = soup.get_text()

# Tokenize the text and count the occurrence of each word in the specified categories
word_count = {}
words = re.findall('\w+', text.lower())
for word in words:
    for category, word_list in categories.items():
        if word in word_list:
            if category not in word_count:
                word_count[category] = {}
            if word not in word_count[category]:
                word_count[category][word] = 0
            word_count[category][word] += 1

# Sort the dictionary by the value of the occurrences in descending order for each category
for category, word_dict in word_count.items():
    sorted_word_count = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    print(f'\n{category}:')
    for i in range(min(3, len(sorted_word_count))):
        print(f'{sorted_word_count[i][0]}: {sorted_word_count[i][1]}')
