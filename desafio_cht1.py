from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setup import init_setup, login, error_message_login
import time

browser = init_setup()

try:

    def case_1(): #Dado que o usuário tenta logar com credenciais incorretas - web
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "email")))
            login("teste1@teste.com","Teste",browser)

            error_message = error_message_login(browser)
            assert "Authentication failed" in error_message.text.strip()
            print("Case 1 executed successfully")
            
        except Exception as e:
            print(f"Erro durante o Caso 1: {e}")

    case_1()

finally:
    time.sleep(2)
    browser.quit()