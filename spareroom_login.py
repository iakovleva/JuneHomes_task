import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException


load_dotenv()
URL = 'https://www.spareroom.com/roommates'

try:
    driver = webdriver.Firefox()
    driver.get(URL)
    login_button = driver.find_element_by_css_selector('div.authentication-links__sign-in-link')
    login_button.click()

    email_field = driver.find_element_by_css_selector('#loginemail')
    email_field.send_keys(os.getenv('EMAIL'))
    password_field = driver.find_element_by_css_selector('#loginpass')
    password_field.send_keys(os.getenv('PASSWORD'))

    submit = driver.find_element_by_css_selector('.sign-in__button')
    submit.submit()

    print('Successfully logged in')

    driver.close()

except (NoSuchElementException, TimeoutException) as error:
    print(error)
