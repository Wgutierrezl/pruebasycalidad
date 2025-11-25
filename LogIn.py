import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ParabankLoginTest(unittest.TestCase):

    def setUp(self):
        #Driver de Chrome
        #self.driver = webdriver.Chrome()

        #Driver de Firefox
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://parabank.parasoft.com/parabank/index.htm")

        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("Password123")
        driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

        # Validación: que el título sea el esperado
        self.assertEqual(driver.title, "ParaBank | Accounts Overview")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()