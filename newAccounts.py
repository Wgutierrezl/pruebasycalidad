import unittest
from selenium import webdriver
import re
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
        driver.get("https://parabank.parasoft.com/parabank/index.html")

        driver.find_element(By.NAME, "username").send_keys("waltg")
        driver.find_element(By.NAME, "password").send_keys("wal")
        driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

        # Validación: que el título sea el esperado
        self.assertEqual(driver.title, "ParaBank | Accounts Overview")
        print("✓ Login exitoso")
        
        
        # 2. HACER CLIC EN NEW ACCOUNT
        driver.find_element(By.LINK_TEXT, "Open New Account").click()
        
        # VALIDAR QUE CARGO LA PAGINA DE NEW ACCOUNT
        open_new_account_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        ).text
        
        
        self.assertEqual(open_new_account_title, "Open New Account")
        print("✓ Página de Open New Account cargada")
        
        
        # OPCIONAL: CREAR CUENTA
        driver.find_element(By.ID, "type").send_keys("CHECKING")
        driver.find_element(By.ID, "fromAccountId").send_keys("13677")

        driver.find_element(By.CSS_SELECTOR, "input[value='Open New Account']").click()
        
        # ESPERAR 10 SEGUNDOS ANTES DE VALIDAR
        print("Esperando 10 segundos para que procese la creación de la cuenta...")
        time.sleep(10)
        
        # Esperar el contenedor que siempre aparece
        result_container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "openAccountResult"))
        )

        # Sacar TODO el texto del contenedor
        result_text = result_container.text

        # Buscar el número con regex
        match = re.search(r"\b\d{4,}\b", result_text)

        self.assertIsNotNone(match, "No se encontró un número de cuenta")

        new_account_number = match.group(0)

        print("✓ Cuenta creada correctamente, nuevo número:", new_account_number)

        self.assertTrue(new_account_number.isdigit())
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()