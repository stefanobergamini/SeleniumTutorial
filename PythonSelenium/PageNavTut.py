from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://github.com/")
driver.maximize_window()

link = driver.find_element_by_link_text("Team")
link.click()


try:
    print("hey oh")
    div_login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".btn-mktg.color-text-white"))
    )
    print("pass the wait")
    print(div_login_button[0])
    div_login_button[0].click()

    driver.back()
    driver.back()
    time.sleep(3)

except:
    print("The End")
    driver.quit()

driver.quit()