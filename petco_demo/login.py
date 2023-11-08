from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os


load_dotenv()
driver = webdriver.Chrome()
actions = ActionChains(driver);

# Let's navigate to the home page
driver.get(os.getenv('BASE_URL'))

# Let's find the header link for login in
elemMiCuenta = driver.find_element(By.CSS_SELECTOR, 'header .nav__links li:nth-child(5)')
# Hover it in order to show the login button
actions.move_to_element(elemMiCuenta)
# Find the login button
elemLogin = driver.find_element(By.CSS_SELECTOR, 'header .nav__links li:nth-child(5) a')
# Click it
actions.click(elemLogin)
# perform all of the actions
actions.perform()

# Let's set a maximum for a wait
wait = WebDriverWait(driver, 10)
# Waiting for email input to be interactable
elemLoginEmail = wait.until(EC.element_to_be_clickable((By.ID, 'j_username')))
# Input user's email
elemLoginEmail.send_keys(os.getenv('USER_EMAIL'))
# Get element for password
elemLoginPassword = wait.until(EC.element_to_be_clickable((By.ID, 'j_password')))
elemLoginPassword.send_keys(os.getenv('USER_PASSWORD'))
# Get log in button
elemLoginButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginForm button')))
elemLoginButton.click()
# Wait for redirect to main page
wait.until(EC.title_contains('Petco Mexico | Petco México'))

# Get text from Hello field
elemUserLoggedIn = driver.find_element(By.CSS_SELECTOR, 'p.textCuenta')
print(elemUserLoggedIn.text)

driver.save_screenshot('screenshot.png')

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
