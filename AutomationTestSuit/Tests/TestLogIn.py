import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
print("Username from .env:", os.getenv("MY_APP_USERNAME"))
print("Password from .env:", os.getenv("MY_APP_PASSWORD"))

# Get username and password from environment variables
username = os.getenv("MY_APP_USERNAME")
password = os.getenv("MY_APP_PASSWORD")

# Set up the ChromeDriver service
#serv_obj = Service("C:/Users/WinBD/PycharmProjects/WooCommerceAutomationTestSuit/AutomationTestSuit/Resources/chromedriver.exe")
#driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()

# Open the URL
driver.get("http://woocommerce-test-site.local/my-account/")

# Wait for the username field to be present
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "username")))

# Enter username and password from environment variables
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

# Click the login button
driver.find_element(By.NAME, "login").click()

# Wait for the page to load and check the title
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'customer-logout')]")))
    print("Login Test Passed")
except:
    print("Login Test Failed")

# Close the browser
driver.quit()
