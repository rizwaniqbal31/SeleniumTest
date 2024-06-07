import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def test_loginPage():
    # Login Page
    driver.get("https://fms-staging.hypernymbiz.com/")


def test_loginSuccessful():
    # Email input field
    email = driver.find_element(By.XPATH,
                                "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[1]/input")
    email.send_keys("hntestfmsri2102@yopmail.com")

    # Password Input field
    password = driver.find_element(By.XPATH,
                                   "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/div[2]/div/input")
    password.send_keys("Aa1234567@")

    # Login Button
    btnLogin = driver.find_element(By.XPATH,
                                   "/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[2]/div/form/button")
    btnLogin.click()

    time.sleep(5)
    driver.close()
    driver.quit()
    print("Done")
