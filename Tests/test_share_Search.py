from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Data import config, imp

email = imp.username
phoneno = config.number
password = imp.password
print("Starting on the earth")


def test_linkedin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in/")
    driver.find_element(By.NAME, "q").send_keys("Rolex")
    driver.find_element(
        By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)