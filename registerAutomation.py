import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ParabankRegistration(unittest.TestCase):

    def setUp(self):
        #Driver de Chrome
        #self.driver = webdriver.Chrome()

        #Driver de Firefox
        self.driver = webdriver.Firefox()

    def test_registration(self):
        driver = self.driver
        driver.get("https://parabank.parasoft.com/")

        # 2. Hacer clic en el enlace de registro
        driver.find_element(By.LINK_TEXT, "Register").click()

        # 3. Completar el formulario de registro
        driver.find_element(By.ID, "customer.firstName").send_keys("Walter")
        driver.find_element(By.ID, "customer.lastName").send_keys("Gutierrez")
        driver.find_element(By.ID, "customer.address.street").send_keys("Calle 123")
        driver.find_element(By.ID, "customer.address.city").send_keys("Medellin")
        driver.find_element(By.ID, "customer.address.state").send_keys("Antioquia")
        driver.find_element(By.ID, "customer.address.zipCode").send_keys("050001")
        driver.find_element(By.ID, "customer.phoneNumber").send_keys("3001234567")
        driver.find_element(By.ID, "customer.ssn").send_keys("123456789")
        driver.find_element(By.ID, "customer.username").send_keys("walterTestUser123")
        driver.find_element(By.ID, "customer.password").send_keys("Password123")
        driver.find_element(By.ID, "repeatedPassword").send_keys("Password123")

        driver.find_element(By.CSS_SELECTOR, "input.button[value='Register']").click()

        # 4. Validar que aparezca un mensaje de éxito
        # Espera explícita para que cargue el mensaje “Welcome”
        success_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.title"))
        ).text

        self.assertIn("Welcome", success_title)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
        