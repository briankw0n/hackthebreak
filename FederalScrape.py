import requests
from bs4 import BeautifulSoup

list = []
url = 'https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=software+developer&locationstring=Vancouver%2C+BC'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

job_listings = soup.find_all('article')

i = 0
for job in job_listings:
    list.append(job.find('span', class_="distance").text.strip())
    list.append(job.find('li', class_="business").text.strip())
    list.append(job.find('li', class_="date").text.strip())
    list.append(job.find('span', class_="wb-inv").text.strip())
    list.append(job.find('span', class_="fa fa-dollar").text.strip())
    list.append(job.a['href'])
    i = i + 1

print(list)