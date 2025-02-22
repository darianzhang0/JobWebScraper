import requests

from bs4 import BeautifulSoup

list_of_jobs = []

## jobsearch() searches indeed.com for jobs. Adds a list containing position, comapany, location and link to more info to list_of_jobs
def jobsearch():
  html_text = requests.get("https://ca.indeed.com/jobs?q=student+developer&l=").text
  soup = BeautifulSoup(html_text, "lxml")
  jobs = soup.find_all('a')
  
  for job in jobs:
    is_job_anchor = False
    job_info = []
    job_name = job.find('h2', class_ = "jobTitle jobTitle-color-purple")
    if job_name != None:
      position = job_name.text.strip()
      is_job_anchor = True
      job_info.append(position)
    
    job_name = job.find('h2', class_ = "jobTitle jobTitle-color-purple jobTitle-newJob")
    if job_name != None:
      position = job_name.text.strip()[3:]
      is_job_anchor = True
      job_info.append(position)

    company_name = job.find('span', class_ = "companyName")
    if company_name != None:
      company = company_name.text.strip()
      is_job_anchor = True
      job_info.append(company)

    location = job.find('div', class_ = "companyLocation")
    if location != None:
      job_location = location.text.strip()
      is_job_anchor = True
      job_info.append(job_location)

    if is_job_anchor:
      more_info = job['href']
      if more_info != None:
        link = "https://ca.indeed.com" + more_info
        job_info.append(link)
    
    if len(job_info) != 0:
      list_of_jobs.append(job_info)
