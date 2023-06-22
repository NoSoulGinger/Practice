import allure
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class TestDropdownList(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        # options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://the-internet.herokuapp.com/dropdown"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-10")
    @allure.title("Dropdown list test")
    def test_dropdown_list(self):
        wait = WebDriverWait(self.browser, 5)
        options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='example']/select[@id='dropdown']/option")))
        select = Select(self.browser.find_element(By.ID, "dropdown"))
        for i in range(1, len(options)):
            select.select_by_value(str(i))
            selected_option = select.first_selected_option
            assert selected_option.text == f"Option {i}"
            print(f"Tested with selecting option {i}. The name of the selected item after selecting is: {selected_option.text}")