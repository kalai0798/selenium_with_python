from selenium import  webdriver
import time
driver=webdriver.chrome()
driver.get("https://www.facebook.com")
time.sleep(5)

print(driver.title)

print(driver.page_source)

print(driver.current_url)

driver.quit()

