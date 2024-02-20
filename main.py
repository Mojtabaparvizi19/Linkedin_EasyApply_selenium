import time
from selenium import webdriver
from selenium.webdriver.common.by import By


keep_open = webdriver.ChromeOptions()
keep_open.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=keep_open)
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(url=url)

sign_in = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
sign_in.click()

user_name_input = driver.find_element(By.ID, value="username")
user_name_input.send_keys("mojtabaparvizi19@gmail.com")

password_input = driver.find_element(By.ID, value="password")
password_input.send_keys("tekken66")

sign_in_button = driver.find_element(By.CSS_SELECTOR, value="div button")
sign_in_button.click()




# easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
# easy_apply.click()
time.sleep(5)

phone_number = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")

listing = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")
for item in listing:
    item.click()
