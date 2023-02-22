from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files\chromedriver.exe"
service = Service(PATH)
driver = WebDriver(service=service)

driver.get("https://absencesub.frontlineeducation.com/Substitute/Home")

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
availableJobs = driver.find_element(By.ID, "availableJobs")
elements = availableJobs.find_elements(By.CLASS_NAME, "job")
jobFound = False
schools = ["TRABUCO HILLS HIGH SCHOOL", "MISSION VIEJO HIGH SCHOOL", "EL TORO HIGH SCHOOL", "LAGUNA HILLS HIGH SCHOOL"]
subjects = ["MATH", "SOCIAL SCIENCE","ENGLISH", "HEALTH", "PHYSICAL EDUCATION", "FOREIGN LANG SPANISH", "ART", "MUSIC"]
for element in elements:
    # print(element)
    locationName = element.find_element(By.CLASS_NAME, "locationName")
    # print(locationName.get_attribute("textContent"))

    if locationName.get_attribute("textContent") in schools:
        highschool = locationName.get_attribute("textContent")
        subjectName = element.find_element(By.CLASS_NAME, "title")
            if subjectName.get_attribute("textContent") in subjects:
                subject_title = subjectName.get_attribute("textContent")
                print(f"{subject_title} available at {highschool}")
                jobFound = True
                break
        # print(locationName)
        # acceptButton = element.find_element(By.CLASS_NAME, "acceptButton")
        # print(acceptButton)

if jobFound == False:
    print("no jobs found")


