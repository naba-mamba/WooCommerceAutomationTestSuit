from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the ChromeDriver service
driver = webdriver.Chrome()
# options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     options=options
# )

# Open the front-end page
driver.get("http://woocommerce-test-site.local/")

try:
    # Wait for the page to load by waiting for the html element
    html_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

    # Check if Dark Mode is already enabled by looking for 'wp-dark-mode-active' and 'wp-dark-mode-animation'
    if "wp-dark-mode-active" in html_element.get_attribute(
            "class") and "wp-dark-mode-animation" in html_element.get_attribute("class"):
        print("Dark Mode is already enabled on the front end.")
    else:
        print("Dark Mode is not enabled. Trying to enable it...")

        # Look for the Dark Mode toggle button using the provided HTML structure
        dark_mode_toggle = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, '_track wp-dark-mode-ignore')]"))
        )
        dark_mode_toggle.click()
        print("Dark Mode toggled.")

        # Re-check the html element to confirm that Dark Mode was enabled
        html_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
        if "wp-dark-mode-active" in html_element.get_attribute(
                "class") and "wp-dark-mode-animation" in html_element.get_attribute("class"):
            print("Dark Mode successfully enabled.")
        else:
            print("Failed to enable Dark Mode.")

except TimeoutException:
    print("Failed to validate Dark Mode functionality.")

finally:
    # Close the browser
    driver.quit()
