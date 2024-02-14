from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Define LinkedIn credentials
LINKEDIN_USERNAME = "YOUR EMAIL"
LINKEDIN_PASSWORD = "YOUR PASSWORD"

# Set Chrome options to keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

# Open a Chrome browser instance
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the LinkedIn Jobs page with specific search criteria
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3655079999&f_AL=true&f_E=1%2C2&geoId=102105699&keywords=Python%20Developer&location=T%C3%BCrkiye&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Find and click on the sign-in button
sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
time.sleep(3)
sign_in.click()
time.sleep(2)

# Enter the LinkedIn username
linkedin_id = driver.find_element(By.NAME, value="session_key")
linkedin_id.send_keys(LINKEDIN_USERNAME)

# Enter the LinkedIn password
linkedin_password = driver.find_element(By.NAME, value="session_password")
linkedin_password.send_keys(LINKEDIN_PASSWORD)

# Click on the sign-in button
linkedin_enter = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
linkedin_enter.click()
time.sleep(12)

# Find all job listings on the page
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Iterate through each job listing
for listing in all_listings:
    # Click on the job listing to view details
    listing.click()
    time.sleep(2)
    # Locate and click the save button
    save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
    save_button.click()
    time.sleep(5)
