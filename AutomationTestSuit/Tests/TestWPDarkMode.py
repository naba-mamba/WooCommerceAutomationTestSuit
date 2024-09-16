from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# Set up the ChromeDriver service
# serv_obj = Service("C:/Program Files/Drivers/chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
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
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'customer-logout')]")))
    print("Login Test Passed")
except TimeoutException:
    print("Login Test Failed")
    driver.quit()

# Now check if "WP Dark Mode" plugin is installed and activated
driver.get("http://woocommerce-test-site.local/wp-admin/plugins.php")

try:
    # Check if the "WP Dark Mode" plugin is active
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//tr[@data-slug='wp-dark-mode']//span[contains(text(), 'Active')]"))
    )
    print("WP Dark Mode Plugin is already active.")
except TimeoutException:
    print("WP Dark Mode Plugin is not active, installing the plugin.")
    # Install WP Dark Mode plugin
    driver.get("http://woocommerce-test-site.local/wp-admin/plugin-install.php")

    # Check if the search box is present and search for the plugin
    search_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "search-plugins")))
    search_box.send_keys("WP Dark Mode")
    search_box.send_keys(Keys.ENTER)

    # Wait for search results and verify the presence of the plugin
    try:
        install_now_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@class='install-now button' and contains(@aria-label, 'WP Dark Mode')]"))
        )
        print("WP Dark Mode Plugin found for installation.")

        # Click Install Now button for the WP Dark Mode plugin
        install_now_button.click()

        # Wait for the 'Activate' button to appear to confirm installation
        try:
            activate_button = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.XPATH,"//a[@class='button activate-now button-primary' and contains(@data-slug, 'wp-dark-mode')]"))
            )
            print("Plugin installed successfully.")
            activate_button.click()  # Activate the plugin
        except TimeoutException:
            print("Failed to find 'Activate' button. Plugin installation might have failed.")
            driver.quit()

    except TimeoutException:
        print("Failed to find WP Dark Mode Plugin in search results.")
        driver.quit()

# Verify the plugin is now active
driver.get("http://woocommerce-test-site.local/wp-admin/plugins.php")

try:
    # Check if the WP Dark Mode plugin is active
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='wp-dark-mode-deactivate-link' and contains(@aria-label, 'Deactivate WP Dark Mode')]"))
    )
    print("WP Dark Mode Plugin is now active.")
except TimeoutException:
    print("WP Dark Mode Plugin is not active.")

# Enable Admin Dashboard Dark Mode
driver.get("http://woocommerce-test-site.local/wp-admin/admin.php?page=wp-dark-mode#/admin")

try:
    # Locate and click the "Enable Admin Dashboard Dark Mode" element
    dark_mode_option = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Enable Admin Dashboard Dark Mode']"))
    )
    dark_mode_option.click()
    print("Admin Dashboard Dark Mode option clicked.")

    # Save settings using the new button element
    save_changes_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Save Changes')]"))
    )
    save_changes_button.click()
    print("Settings saved.")
except TimeoutException:
    print("Failed to enable Admin Dashboard Dark Mode.")
    driver.quit()
    exit()

# Validate Dark Mode
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//body[contains(@class, 'dark-mode')]"))
    )
    print("Admin Dashboard Dark Mode is enabled.")
except TimeoutException:
    print("Failed to enable Admin Dashboard Dark Mode.")
    driver.quit()




# Close the browser
driver.quit()
