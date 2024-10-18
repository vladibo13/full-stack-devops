from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = '../../../../chrome-driver/chromedriver/chromedriver'

# Replace 'path_to_chromedriver' with the path to your local ChromeDriver.
service = Service(executable_path=CHROME_DRIVER_PATH)

# 1. Start a Selenium WebDriver session.
driver = webdriver.Chrome(service=service)

try:
    # 2. Navigate to web interface URL with a user ID (replace with the actual URL and user ID logic).
    url = "http://localhost:5173/"  # Replace with your web interface URL.
    user_id = "1"  # Example user ID, if needed for the URL or login.

    driver.get(url)

    # Optional: If login is required, you can add login steps here.
    # Example:
    # driver.find_element(By.NAME, "username").send_keys(user_id)
    # driver.find_element(By.NAME, "password").send_keys("your_password")
    # driver.find_element(By.NAME, "login").click()

    time.sleep(3)  # Wait for the page to load fully.

    # 3. Check that the user name element exists (replace with your specific locator).
    user_name_locator = (By.ID, "user-id-1")  # Adjust the locator as needed (ID, class, etc.).

    # Find the user name element.
    user_name_element = driver.find_element(*user_name_locator)

    # 4. Print the user name.
    if user_name_element:
        print("User Name:", user_name_element.text)
    else:
        print("User name element not found.")
finally:
    # Close the browser session.
    driver.quit()