from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shadow_root():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("http://watir.com/examples/shadow_dom.html")
    driver.implicitly_wait(10)

    root = driver.find_element(By.CSS_SELECTOR, '[id="shadow_host"]').shadow_root
    shadow_text = root.find_element(By.CSS_SELECTOR, '[id="shadow_content"]').text
    print(shadow_text)

    inner_shadow_root = root.find_element(By.CSS_SELECTOR, '[id="nested_shadow_host"]').shadow_root
    inner_shadow_text = inner_shadow_root.find_element(By.CSS_SELECTOR, '[id="nested_shadow_content"]').text
    print(inner_shadow_text)
