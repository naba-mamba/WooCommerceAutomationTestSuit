import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the username and password from environment variables
username = os.getenv("MY_APP_USERNAME")
password = os.getenv("MY_APP_PASSWORD")

# Set up the ChromeDriver service
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Open the login page
driver.get("http://woocommerce-test-site.local/my-account/")

# Wait for the username field to be present
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "username")))

# Enter username and password
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

# Click the login button
driver.find_element(By.NAME, "login").click()

# Wait for the page to load and check if login was successful
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'customer-logout')]"))
    )
    print("Login Test Passed")
except TimeoutException:
    print("Login Test Failed")
    driver.quit()
    exit()

# Enable Admin Dashboard Dark Mode
driver.get("http://woocommerce-test-site.local/wp-admin/admin.php?page=wp-dark-mode#/admin")

try:
    # Wait for the dark mode option to be clickable and then click it
    dark_mode_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Enable Admin Dashboard Dark Mode']"))
    )
    dark_mode_option.click()
    print("Admin Dashboard Dark Mode option clicked.")

    # Wait for the save button to be clickable and then click it
    save_changes_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Save Changes']"))
    )
    save_changes_button.click()
    print("Settings saved.")
except TimeoutException:
    print("Failed to enable Admin Dashboard Dark Mode.")
    driver.quit()
    exit()

# Validate Dark Mode
try:
    # Wait for the body to have the dark mode class
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//body[contains(@class, 'dark-mode')]"))
    )
    print("Admin Dashboard Dark Mode is enabled.")
except TimeoutException:
    print("Failed to enable Admin Dashboard Dark Mode.")

# Close the browser
driver.quit()
