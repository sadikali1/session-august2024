import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
#driver = webdriver.Edge()

driver.get('https://www.facebook.com/')

email_input = driver.find_element(By.ID, "email")
email_input.clear()
email_input.send_keys("test@text.com")

pass_input = driver.find_element(By.ID, "pass")
pass_input.send_keys("test123456")

driver.find_element(By.NAME, "login").click()

# id, name, classname, tagname, xpath, css Selector, link text, partial link text



#driver.quit()

# element, locator

# Html -- tags and attribute

# webelement