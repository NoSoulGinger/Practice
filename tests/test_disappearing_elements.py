import allure
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestDisappearingElements(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://the-internet.herokuapp.com/disappearing_elements"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-09")
    @allure.title("Disappearing Elements test")
    def test_disappearing_elements(self):
        list_of_elements = []
        wait = WebDriverWait(self.browser, 5)
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul/li")))
        for element in elements:
            list_of_elements.append(element.text)
        print(f"Before refresh the page has {len(elements)} elements.\nThe elements are the following: {list_of_elements}")
        assert len(elements) == 4
        list_of_elements.clear()
        self.browser.refresh()
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul/li")))
        for element in elements:
            list_of_elements.append(element.text)
        print(f"After refresh the page has {len(elements)} elements.\nThe elements are the following: {list_of_elements}")
        assert len(elements) == 5