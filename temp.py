from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Use the correct WebDriver for your browser
driver.get("https://sellercentral.amazon.in/spec/productcompliance/form?clientName=spec_web")

# Log in to Amazon Seller Central manually
# input("Log in to Amazon Seller Central and press Enter once ready...")

try:
    # Wait for the page to load completely
    time.sleep(5)

    # Locate the dropdown container by class name
    dropdown_container = driver.find_element(By.CLASS_NAME, "css-1x9fncp-indicatorContainer")
    
    # Click on the dropdown to reveal options
    dropdown_container.click()
    time.sleep(2)  # Allow options to load

    # Locate the dropdown options (adjust the locator if necessary)
    options = driver.find_elements(By.CSS_SELECTOR, " css-26l3qy-menu")  # Adjust selector if options have a specific class

    # Extract text from each option
    categories = [option.text for option in options]

    # Print the product categories
    print("Product Categories:")
    for category in categories:
        print(category)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
