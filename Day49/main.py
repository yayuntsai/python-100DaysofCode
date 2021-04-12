from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "./chromedriver"
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)
my_email = MY_EMAIL_VAL
my_password = MY_PASSWORD_VAL


chrome_driver.get('https://www.linkedin.com')
login_btn = chrome_driver.find_element_by_class_name("nav__button-secondary")
login_btn.click()
email = chrome_driver.find_element_by_id("username")
password = chrome_driver.find_element_by_id("password")
email.send_keys(MY_EMAIL_VAL)
password.send_keys(MY_PASSWORD_VAL)
button = chrome_driver.find_element_by_css_selector(".login__form_action_container button")
button.click()

#Wait for the next page to load.
time.sleep(5)


# go to apply page
chrome_driver.get('https://careers.google.com/jobs/results/129172490308985542-software-engineer-chrome-os/?src=Online%2FLinkedIn%2Flinkedin_us&utm_campaign=contract&utm_medium=jobposting&utm_source=linkedin')
time.sleep(6)
apply_btn = chrome_driver.find_element_by_id("ember433")
apply_btn.click()
continue_btn = chrome_driver.find_element_by_id("ember2224")
continue_btn.click()