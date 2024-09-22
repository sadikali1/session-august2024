from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def test_facebook_signup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    driver.get('https://www.facebook.com/')
    #driver.find_element(By.LINK_TEXT, 'Create new account').click()
    driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']").click()
    #time.sleep(2)
    driver.find_element(By.NAME, "firstname").send_keys("QA")
    driver.find_element(By.NAME, "lastname").send_keys("Automation")
    driver.find_element(By.NAME, "reg_email__").send_keys("test@test.com")
    driver.find_element(By.ID, "password_step_input").send_keys("Password")

    select_date = Select(driver.find_element(By.ID, "day"))
    select_date.select_by_visible_text("20")

    select_date = Select(driver.find_element(By.ID, "month"))
    # select_date.select_by_visible_text("Feb")
    #select_date.select_by_index(5)
    select_date.select_by_value("7")

    select_date = Select(driver.find_element(By.ID, "year"))
    # select_date.select_by_visible_text("2003")
    select_date.select_by_index(2)

    status = driver.find_element(By.XPATH, "//input[@value='2']").is_selected()
    print(status)
    driver.find_element(By.XPATH, "//input[@value='2']").click()
    status = driver.find_element(By.XPATH, "//input[@value='2']").is_selected()
    print(status)

# Implicit Wait
# Explicit Wait
