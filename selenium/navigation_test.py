from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_navigatiion():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://demoqa.com/browser-windows')

    driver.get('https://facebook.com')
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()


# By.Id, By.Name, By.ClassName, By.TabName, By.CssSelector, By.Xpath, By.LinkText, By.PartialLinkText

#alert = Alert(driver) - alert.accept(), alert.dismiss(), alert.text, alert.send_keys()
