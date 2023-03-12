import requests
from bs4 import BeautifulSoup

def get_jobDescription(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('article') 

    jobs = []

    for job in job_listings:
        title = job.find('span', class_='noctitle').text.strip()
        company = job.find('li', class_='business').text.strip()
        link = job.find('a')['href']

        link = link.split(';')[0]
        
        jobs.append({
            'title': title,
            'company': company,
            'link': link
        })

    return jobs
