import allure
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class TestContextMenu(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://the-internet.herokuapp.com/context_menu"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-08")
    @allure.title("Context menu test")
    def test_context_menu(self):
        action = ActionChains(self.browser)
        wait = WebDriverWait(self.browser, 5)
        box = wait.until(EC.presence_of_element_located((By.ID, "hot-spot")))
        action.context_click(box).perform()
        alert = self.browser.switch_to.alert
        assert alert.text == "You selected a context menu"