import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("http://google.com")
    time.sleep(2)
    driver.close()
    driver.quit()
    print("Done")
