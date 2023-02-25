from flask import Flask

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from twilio.rest import Client

account_sid = 'AC8c7f8fcb6b0418e5882193f3143676d0'
auth_token = '30b7a8b1e7a7081257e0f7f84738b144'

cl = Client(account_sid, auth_token)

import time
import sys

app = Flask(__main__)


@app.route('/')
def run_script():
    PATH = "C:\Program Files\chromedriver.exe"
    service = Service(PATH)
    driver = WebDriver(service=service)

    driver.get("https://absencesub.frontlineeducation.com/Substitute/Home")
    driver.minimize_window()
    time.sleep(10)

    username = driver.find_element(By.ID, 'Username')
    username.clear()
    username.send_keys("rpapazian41")

    time.sleep(2)

    password = driver.find_element(By.ID, 'Password')
    password.clear()
    password.send_keys("Flyersfan4!")

    time.sleep(2)

    password.send_keys(Keys.RETURN)

    time.sleep(10)

    for i in range(12):
        availableJobs = driver.find_element(By.ID, "availableJobs")
        elements = availableJobs.find_elements(By.CLASS_NAME, "job")
        jobFound = False
        schools = ["TRABUCO HILLS HIGH SCHOOL", "MISSION VIEJO HIGH SCHOOL", "EL TORO HIGH SCHOOL",
                   "LAGUNA HILLS HIGH SCHOOL"]
        subjects = ["MATH", "SOCIAL SCIENCE", "SCIENCE - BIOLOGY", "SCIENCE - CHEMISTRY", "SCIENCE - PHYSICS",
                    "ENGLISH", "HEALTH", "TECH ED - VIDEO", "TECH ED - PHOTO", "DRAMA/THEATER", "FOREIGN LANG SPANISH",
                    "ART", "MUSIC", "PHYSICAL EDUCATION"]
        for element in elements:
            locationName = element.find_element(By.CLASS_NAME, "locationName")

            if locationName.get_attribute("textContent") in schools:
                highschool = locationName.get_attribute("textContent")

                subjectName = element.find_element(By.CLASS_NAME, "title")

                if subjectName.get_attribute("textContent") in subjects:
                    subject_title = subjectName.get_attribute("textContent")
                    print(f"{subject_title} available at {highschool}")
                    jobFound = True
                    break

        if jobFound == False:
            print("No jobs found")
        else:

            message = cl.messages.create(
                body='Look at new job',
                from_='+18333620451',
                to='+19496977678'
            )

            print(message.sid)
            driver.quit()
            return "Script successfully ran and message sent!"

        time.sleep(300)
        driver.refresh()
        time.sleep(30)

    driver.quit()
    return "No jobs found after 12 attempts."
