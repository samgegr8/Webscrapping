import requests
from bs4 import BeautifulSoup

location = input("Please enter the job search Location ::")

URL = "https://www.monster.com/jobs/search/?q=Software-Developer&where=" + location


page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

"""print(results.prettify()) """

"""To Extract All the Job returned from the Query String """

job_elemens = results.find_all("section", class_="card-content")
count = 1
for job_elem in job_elemens:
    # print(f"Job Elem :{count} {job_elem}\n")
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("div", class_="company")
    location_elem = job_elem.find("div", class_="location")
    if None in (title_elem, company_elem, location_elem):
        continue
    print(f"Item :: {count} \n\n")
    # Text command is used to get the value of the element gone
    print(f"Title : { title_elem.text.strip()}\n")
    print(f"Company : {company_elem.text.strip()}\n")
    print(f"Location : {location_elem.text.strip()}\n")
    count = count + 1

# Modifying the Script to do an exact search
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
# print(f"Python Details :: {python_jobs}")
count = 0
for p_jobs in python_jobs:
    print(f"Python Details :: {p_jobs.find('a')['href']}")
    count = count + 1
if count == 0:
    print(f"No Python Job in {location}")
