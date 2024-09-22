from selenium import webdriver
from selenium.webdriver.common.by import By

def test_table_data():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://the-internet.herokuapp.com/tables")

    driver.find_element(By.XPATH, "//span[text()='Last Name']").click()
    driver.find_element(By.XPATH, "//span[text()='Last Name']").click()

    list_element = driver.find_elements(By.XPATH, '//table[@id="table1"]/tbody/tr/td[3]')

    i = 1
    status = False
    for element in list_element:
        email = element.text
        if email == "fbach@yahoo.com":
            driver.find_element(By.XPATH, '//*[@id="table1"]/tbody/tr['+str(i)+']/td[6]/a').click()
            status = True
            break
        i +=1
    assert status == True

# Page Object Model