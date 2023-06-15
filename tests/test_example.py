from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestTeglalap(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/teglalap_kerulet.html"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.id("TC-01")
    @allure.title("Web test")
    def test_one(self):
        def fill_data(a_data, b_data, exp_result):
            wait = WebDriverWait(self.browser, 2)
            a = self.browser.find_element(By.ID, "a")
            b = self.browser.find_element(By.ID, "b")
            calculate = self.browser.find_element(By.ID, "submit")

            a.clear()
            b.clear()
            a.send_keys(a_data)
            b.send_keys(b_data)
            calculate.click()
            result = wait.until(EC.presence_of_element_located((By.ID, "result")))
            assert result.text == exp_result

        test_data = [
            {"a": "74", "b": "32", "exp_result": "212"},
            {"a": "kiskutya", "b": "32", "exp_result": "NaN"},
            {"a": "", "b": "", "exp_result": "NaN"},
        ]

        for test_data in test_data:
            fill_data(test_data["a"], test_data["b"], test_data["exp_result"])
