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
    driver.find_element(
        By.XPATH, "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']").click()
    driver.find_element(
        By.XPATH, "//button[@title='Share this page on Linkedin New tab']//span[@class='sc-AxjAm oUQss']//*[name()='svg']//*[name()='path' and contains(@d,'m15 8.91v5')]").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//*[@id="username"]').click()
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(phoneno)
    driver.find_element(By.XPATH, "//input[@id='password']").click()
    driver.find_element(
        By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@aria-label='Sign in']").click()
    driver.maximize_window()
    time.sleep(20)
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Share in a post']").click()