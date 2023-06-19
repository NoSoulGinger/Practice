import time
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAddElementButton(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://the-internet.herokuapp.com/add_remove_elements/"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-06")
    @allure.title("Add and remove element button test")
    def test_adding_elements(self):
        wait = WebDriverWait(self.browser, 5)
        add_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='example']/button")))
        clicks = 5
        for i in range(clicks):
            add_element.click()
        element_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='elements']/button[@class='added-manually']")))
        print(f"The test was run by clicking the add element button {clicks} times.\nThe number of visible new buttons after the clicks: {len(element_list)}")
        assert len(element_list) == clicks