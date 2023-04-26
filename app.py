from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

browser = webdriver.Firefox()
browser.get('https://rozetka.com.ua/')
time.sleep(5) 

dom_input = browser.find_element(By.NAME, 'search' )
dom_input.send_keys("Lenovo")
time.sleep(10)

ActionChains(browser).key_down(value=Keys.ENTER).perform()
time.sleep(10)

browser.quit()