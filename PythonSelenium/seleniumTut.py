#seguindo o tutorial

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim")
print(driver.title)

driver.quit()

