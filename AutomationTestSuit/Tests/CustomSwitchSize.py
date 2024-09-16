import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Load environment variables from .env file
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

# Navigate to WP Dark Mode
driver.get("http://woocommerce-test-site.local/wp-admin/admin.php?page=wp-dark-mode#/frontend")

try:
    # Click "Customization"
    customization_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center gap-3']//h4[text()='Customization']"))
    )
    customization_option.click()
    print("Customization clicked.")

    # Click "Switch Settings"
    switch_settings = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Switch Settings']"))
    )
    switch_settings.click()
    print("Switch Settings clicked.")

    # Select Custom Switch Size
    custom_size_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Custom']"))
    )
    custom_size_option.click()
    print("Custom size option clicked.")

    # Adjust the scale to 220 using JavaScript
    scale_slider = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='range' and @min='50' and @max='300']"))
    )
    driver.execute_script("arguments[0].value = 220;", scale_slider)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", scale_slider)
    print("Switch scaled to 220.")

    # Save settings using the "Save Changes" button
    save_changes_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'bg-blue-500') and contains(@class, 'text-white') and text()='Save Changes']")
        )
    )
    save_changes_button.click()
    print("Settings saved.")
except TimeoutException:
    print("Failed to change Switch Customization.")
finally:
    # Close the browser
    driver.quit()
