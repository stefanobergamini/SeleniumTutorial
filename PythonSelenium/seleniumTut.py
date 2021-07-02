#seguindo o tutorial

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.github.com/")
print(driver.title)
driver.maximize_window()

search_bar = driver.find_element_by_name("q")
search_bar.send_keys("selenium")
time.sleep(1)
search_bar.send_keys(Keys.RETURN)

try:
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "repo-list"))
    )

    titles = search_results.find_elements_by_class_name("mt-n1")
    for title in titles:
        name = title.find_element_by_class_name("v-align-middle")
        print(name.text)
finally:
    print("The End")
    driver.quit()


