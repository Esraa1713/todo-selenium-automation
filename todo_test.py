from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

service = Service('C:/webdrivers/chromedriver.exe')

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

service = Service("C:\\Users\\Omar\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)

driver.get("https://todomvc.com/examples/react/dist/")
try:
    time.sleep(2)

    task_input = driver.find_element(By.CLASS_NAME, "new-todo")
    task_input.send_keys("Buy Milk")
    time.sleep(1)
    task_input.send_keys(Keys.ENTER)

    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[.='Buy Milk']"))
    )

    complete_checkbox = driver.find_element(By.CSS_SELECTOR, "input.toggle")
    complete_checkbox.click()

    time.sleep(2)

    todo_item = driver.find_element(By.XPATH, "//label[.='Buy Milk']")
    driver.execute_script("arguments[0].scrollIntoView();", todo_item)
    webdriver.ActionChains(driver).move_to_element(todo_item).perform()

    time.sleep(1)

    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "destroy"))
    )
    delete_button.click()

    time.sleep(5)

finally:
    driver.quit()