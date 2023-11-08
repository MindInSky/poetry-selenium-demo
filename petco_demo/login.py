from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os


load_dotenv()
driver = webdriver.Chrome()
# driver.set_window_size(1920, 1080)
actions = ActionChains(driver);

# Let's set a maximum for a wait
wait = WebDriverWait(driver, 15)

#Let's put all the user info here:
userFirstName = os.getenv('USER_FIRST_NAME')
userFirstLastName= os.getenv('USER_FIRST_LASTNAME')
userSecondLastName= os.getenv('USER_SECOND_LASTNAME')
userZipCode= os.getenv('USER_ZIPCODE')
userColonia= os.getenv('USER_COLONIA')
userCalle= os.getenv('USER_CALLE')
userNumExt= os.getenv('USER_NUMERO_EXT')
userPhone= os.getenv('USER_PHONE')
userReference = os.getenv('USER_REFERENCE')
userStreetA = os.getenv('USER_STREET_A')
userStreetB = os.getenv('USER_STREET_B')

# Let's navigate to the home page
driver.get(os.getenv('BASE_URL'))

# Let's find the header link for login in
elemMiCuenta = driver.find_element(By.CSS_SELECTOR, 'header .nav__links li:nth-child(5)')
# Hover it in order to show the login button
actions.move_to_element(elemMiCuenta).perform()
# Find the login button
elemLogin = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'header .nav__links li:nth-child(5) a')))
# Click it
# elemLogin.click()
elemLogin.click()

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

# I'm checking that the user's name is reflected on the site
# to confirm the log in worked
try:

  assert userFirstName in elemUserLoggedIn.text

except AssertionError as e:

  print('Error in login: ', e)

else:

  print('Logged in')

#Move through the nav menu
elemMascotasDropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.auto.nav__links--primary.nav-drop.petco-open')))
actions.move_to_element(elemMascotasDropdown).perform()
elemMamiferosNav = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-hierarchy="MamiferosNavNode"]')))
elemMamiferosNav.click()

#Confirm we navigated
wait.until(EC.url_contains, 'Mamíferos')

elemMamiferoProduct = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-item')))
elemMamiferoProduct.click()

elemAddToCartBttn = wait.until(EC.element_to_be_clickable((By.ID,'addToCartButton')))
elemAddToCartBttn.click()

wait.until(EC.title_contains('Mi Carrito'))

try:

  assert 'cart' in driver.current_url

except AssertionError as e:
  print('Error adding to cart: ', e)

else:
  print('Added Mamiferos item to cart')

#Move through the nav menu
elemMascotasDropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.auto.nav__links--primary.nav-drop.petco-open')))
actions.move_to_element(elemMascotasDropdown).perform()
elemPerrosNav = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-hierarchy="PerroNavNode"]')))
elemPerrosNav.click()

elemPerroProduct = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-item')))
elemPerroProduct.click()

elemAddToCartBttn = wait.until(EC.element_to_be_clickable((By.ID,'addToCartButton')))
elemAddToCartBttn.click()

wait.until(EC.title_contains('Mi Carrito'))

try:
  assert 'cart' in driver.current_url

except AssertionError as e:
  print('Error adding to cart: ', e)
else:
  print('Added Perro item to cart')

#Wait until we are back in the cart
wait.until(EC.title_contains('Mi Carrito'))


#Let's finish the purchase
btnContinueCheckout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.btn--continue-checkout')))
actions.scroll_by_amount(0,200).perform() #needed as in 1240 resolution this button is covered by the chat button
btnContinueCheckout.click()


try:
  assert 'checkout' in driver.current_url

except AssertionError as e:
  print('Error getting to checkout: ', e)
else:
  print('In checkout page')

# btnNewAddress = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[id="sp-address-coll"] button[ng-click="displayAddressForm(true)"]')))
# Loading of the page makes this element stale, need to retry
try:
  btnNewAddress = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sp-address-coll"]/div/div[2]/div/div[3]/button')))
  btnNewAddress.click()
except Exception as e :
  btnNewAddress = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sp-address-coll"]/div/div[2]/div/div[3]/button')))
finally :
  btnNewAddress.click()

# Input First Name
inputFirstName = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.firstName"]')))
inputFirstName.send_keys(userFirstName)

# Input First Last Name
inputFirstLastName = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.middleName"]')))
inputFirstLastName.send_keys(userFirstLastName)

# Input Second Last Name
inputSecondLastName = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.lastName"]')))
inputSecondLastName.send_keys(userSecondLastName)

# Input ZipCode
inputZipCode = wait.until(EC.element_to_be_clickable((By.ID, 'postalCodeInput')))
inputZipCode.send_keys(userZipCode)
inputZipCode.send_keys(Keys.RETURN)

selectColonia = Select(wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[ng-model="addressForm.district"]'))))
selectColonia.select_by_visible_text(userColonia)

inputCalle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.line1"]')))
inputCalle.send_keys(userCalle)

inputCalleNum = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.line2"]')))
inputCalleNum.send_keys(userNumExt)

inputPhone = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.phone"]')))
inputPhone.send_keys(userPhone)

inputRerefence = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.reference"]')))
inputRerefence.send_keys(userReference)

inputBetweenA = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.betweenStreet1"]')))
inputBetweenA.send_keys(userStreetA)

inputBetweenB = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[ng-model="addressForm.betweenStreet2"]')))
inputBetweenB.send_keys(userStreetB)

# Saving a screenshot when the test finishes, just to confirm
driver.save_screenshot('screenshot2.png')
