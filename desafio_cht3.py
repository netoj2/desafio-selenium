# 3. Teste de Cadastro com Dados Inválidos
# Dado:
# 	• O formulário de cadastro está disponível e requer um e-mail válido para criar uma conta.
# Quando:
# 	• O usuário tenta se cadastrar com um e-mail inválido.
# 	E-mail: teste@teste
# Então:
#   • O sistema rejeita o e-mail inválido e exibe uma mensagem de dizendo "Invalid email address." indicando que o endereço de e-mail é inválido.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setup import init_setup
import time

browser = init_setup(mobile=False)

try:

    def case_3():
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "email_create")))
            browser.find_element(By.ID, "email_create").send_keys("teste@teste")
            browser.find_element(By.NAME, "SubmitCreate").click()

            error_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#create_account_error ol li"))
            )
            assert "Invalid email address." in error_element.text
            print("Case 3 executed successfully")

        except Exception as e:
            print(f"Error during Case 1: {e}")

    case_3()

finally:
    time.sleep(2)
    browser.quit()