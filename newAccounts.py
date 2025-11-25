import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ParaBankNewAccount(unittest.TestCase):

    def setUp(self):
        #Driver de Chrome
        #self.driver = webdriver.Chrome()

        #Driver de Firefox
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://parabank.parasoft.com")

        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("Password123")
        driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()
  
        # 2. HACER CLIC EN NEW ACCOUNT
        driver.find_element(By.LINK_TEXT, "Open New Account").click()
        
        # VALIDAR QUE CARGO LA PAGINA DE NEW ACCOUNT
        open_new_account_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        ).text
        
        self.assertEqual(open_new_account_title, "Open New Account")
           
        # CREAR CUENTA
        driver.find_element(By.ID, "type").send_keys("CHECKING")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[value='Open New Account']").click()
        time.sleep(1)
        
        confirmation = driver.find_element(By.ID, "newAccountId")
        self.assertTrue(driver.title, "ParaBank | Account Opened!")
        
        print("New account created with ID:", confirmation.text)

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()