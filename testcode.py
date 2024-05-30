import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize webdriver
driver = webdriver.Chrome()

# Open URL and maximize window
driver.get('https://websitedemos.net/custom-printing-02/')


driver.maximize_window()
def wait_for_element(locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
about_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="menu-link" and text()="About"]')))
about_link.click()
time.sleep(2)
contact_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="menu-link" and text()="Contact"]')))
contact_link.click()
time.sleep(2)

all_products_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="menu-link" and text()="All Products"]')))

all_products_link.click()
product_link = driver.find_element(By.CLASS_NAME, 'woocommerce-LoopProduct-link')

# Click on the anchor element to navigate to the next page
product_link.click()
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')
time.sleep(2)

add_to_cart_button = driver.find_element(By.NAME, "add-to-cart")
add_to_cart_button.click()
time.sleep(2)
all_products_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="menu-link" and text()="All Products"]'))
    )
all_products_link.click()
tshirts_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='woocommerce_product_categories-3']//a[text()='Tshirts']"))
    )

    # Click on the "Tshirts" link
tshirts_link.click()
image_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-LoopProduct-link"))
    )

    # Click on the image link
image_link.click()
time.sleep(2)
#quantity_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "quantity_663e464a8f236")))

    # Clear the current value and set it to 2
#quantity_input.clear()
#quantity_input.send_keys("2")
add_to_cart_button = driver.find_element(By.NAME, "add-to-cart")
add_to_cart_button.click()
view_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "wc-forward"))
    )

    # Click on the "View cart" button
view_cart_button.click()
time.sleep(2)
checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))
    )

checkout_button.click()
input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "billing_first_name"))
    )
input_field.clear()
time.sleep(1)
input_field.send_keys("Sivaraman")
time.sleep(1)
input_field1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "billing_last_name"))
    )
input_field1.clear()
time.sleep(1)
input_field1.send_keys("Narayanaswamy")
time.sleep(1)
input_field2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "billing_address_1"))
    )
input_field2.clear()
time.sleep(1)
input_field2.send_keys("12 a selvam nagar Kovaipudur")
time.sleep(1)
input_field3 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "billing_city"))
    )
input_field3.clear()
time.sleep(1)
input_field3.send_keys("coimbatore")
time.sleep(1)
dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "select2-billing_state-container"))
    )

    # Click on the dropdown to open the options
dropdown_element.click()

    # Locate the desired option within the dropdown options
option_to_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[text()='Tamil Nadu']"))
    )

    # Click on the desired option to select it
option_to_select.click()
input_field5 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "billing_postcode"))
    )
input_field5.clear()
time.sleep(1)
input_field5.send_keys("641042")
time.sleep(1)
input_field6 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "billing_phone"))
    )
input_field6.clear()
time.sleep(1)
input_field6.send_keys("9894748665")
time.sleep(1)
input_field7 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "billing_email"))
    )
input_field7.clear()
time.sleep(1)
input_field7.send_keys("abinayavarshini220903@gmail.com")
time.sleep(1)
place_order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "place_order"))
    )

    
place_order_button.click()
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')
