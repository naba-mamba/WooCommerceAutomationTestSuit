from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the ChromeDriver service
driver = webdriver.Chrome()

# Open the login page
driver.get("http://woocommerce-test-site.local/my-account/")

# Wait for the username field to be present
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "username")))

# Enter username and password
driver.find_element(By.NAME, "username").send_keys("Fairuznaba03@gmail.com")
driver.find_element(By.NAME, "password").send_keys("naba2000")

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

    # Click "Site Animation"
    site_animation_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Site Animation']"))
    )
    site_animation_option.click()
    print("Site Animation clicked.")

    # Enable "Page Transition Animation"
    enable_page_transition = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Enable Page Transition Animation']"))
    )
    enable_page_transition.click()
    print("Page Transition Animation enabled.")

    # Select an animation other than default (other than "Flip")
    animation_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Flip']"))
    )
    animation_option.click()
    print("Animation Effect 'Flip' selected.")

    # Save settings using the "Save Changes" button
    save_changes_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'bg-blue-500') and contains(@class, 'text-white') and text()='Save Changes']")
        )
    )
    save_changes_button.click()
    print("Settings saved.")
except TimeoutException:
    print("Failed to change Site Animation settings.")
finally:
    # Close the browser
    driver.quit()
