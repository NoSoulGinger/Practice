import time
import requests
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestBrokenImage(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        # options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://the-internet.herokuapp.com/broken_images"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-07")
    @allure.title("Broken image test")
    def test_broken_image_test(self):
        BrokenImageCount = 0
        wait = WebDriverWait(self.browser, 5)
        images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
        print(f"Total number of image on the website are {len(images)}")
        for img in images:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if (response.status_code != 200):
                    print(img.get_attribute('outerHTML') + " is broken.")
                    BrokenImageCount += 1
            except:
                print(img.get_attribute('outerHTML') + " is not broken.")
        print(f'The page has {BrokenImageCount} broken images')
        assert BrokenImageCount == 0