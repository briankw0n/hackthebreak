import requests
from bs4 import BeautifulSoup

def get_jobDescription(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('article')

    list = []

    for job in job_listings:
        distance = job.find('span', class_="distance").text.strip()
        company = job.find('li', class_="business").text.strip()
        postdate = job.find('li', class_="date").text.strip()
        temp = job.find('li', class_="location").text.strip().replace("\n", "")
        temp = temp.replace("\t", "")
        temp = temp.replace("Location", "")
        temp = temp.replace(" ", "")
        location = temp
        postURL = job.a['href']
        list.append({
            'distance': distance,
            'company': company,
            'postdate': postdate,
            'location': location,
            'postURL': postURL
        })

    return list
