import requests
from bs4 import BeautifulSoup
import json

careers = {}

key = []

list = []

url = 'https://jobpersonality.co.uk/alphabetical-profession-list'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

job_listings = soup.find_all('div', class_="text-block")
for job in job_listings:
    list.append(job.find('p').text)

# careers[key] = list
# final = json.dumps(careers, indent=2)
print(list)
