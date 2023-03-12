import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser

def get_job_description(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  job_listings = soup.find_all('a', class_='list-item-wrapper')

  jobs = []

  for job in job_listings:
      title = job.find('div', class_='list-item-title').text.strip()
      company = job.find('div', class_='list-divider').text.strip()
      link = job.get('href')

      jobs.append({
          'title': title,
          'company': company,
          'link': link
      })

  return jobs
