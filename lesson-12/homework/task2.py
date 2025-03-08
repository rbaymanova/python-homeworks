import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        application_link TEXT,
        UNIQUE(title, company, location)
    )
""")

job_listings = soup.find_all("div", class_="card-content")
new_jobs = []

for job in job_listings:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    description_tag = job.find("div", class_="description")
    description = description_tag.text.strip() if description_tag else "No description available"

    application_link_tag = job.find("a", class_="apply")
    application_link = application_link_tag.get("href") if application_link_tag else "No link available"

    cursor.execute("SELECT * FROM jobs WHERE title=? AND company=? AND location=?", (title, company, location))
    
    if not cursor.fetchone():
        cursor.execute("INSERT INTO jobs (title, company, location, description, application_link) VALUES (?, ?, ?, ?, ?)",
                       (title, company, location, description, application_link))
        new_jobs.append((title, company, location, description, application_link))

conn.commit()

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Description", "Application Link"])
    writer.writerows(new_jobs)

conn.close()
