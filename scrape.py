import requests
from bs4 import BeautifulSoup

url = 'https://www.bcjobs.ca/search-jobs?q=software+developer&location='
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

job_listings = soup.find_all('div', id='joblist-body-content')

for job in job_listings:
    title = job.find('div', class_='list-item-title').text.strip()
    company = job.find('div', class_='list-divider').text.strip()
    link = job.find('a', href=True)['href']

    print(f"Title: {title}")
    print(f"Company: {company}")
    print(f"Link: {link}")
    print()
    

##div_elements = soup.find_all('div', class_='u_p-none')
##
##for div in div_elements:
##    title = div.find('div', class_='list-item-title')
##    company = div.find('div', class_='text-limit')
##    link = div.find('a', href=True)['href']
##
##    print(title)
##    print(company)
##    print(link)
    
