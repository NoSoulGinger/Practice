import time
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSelect(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://the-internet.herokuapp.com/checkboxes"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-01")
    @allure.title("Web listing test")
    def test_numberone(self):
        wait = WebDriverWait(self.browser, 5)
        list = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox']")
            )
        )
        list[0].click()
        list[1].click()
        assert list[0].is_selected()
        assert list[1].is_selected() == False
