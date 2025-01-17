# 2. Teste de Login com Credenciais Incorretas - Mobile
# Dado:
# 	• O usuário possui um formulário de login com campos para e-mail e senha.
# 	• O sistema está funcionando e esperando as credenciais do usuário, no mobile: Iphone X.
# Quando:
# 	• O usuário tenta fazer login com um e-mail e senha incorretos.
# 	E-mail: teste1@teste.com
# 	Senha: Teste
# Então:
# 	• O sistema não permite o login e exibe uma mensagem de erro dizendo "Authentication failed", garantindo que apenas credenciais corretas possam acessar a conta.


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setup import init_setup, login, error_message_login
import time

browser = init_setup(mobile=True)

try:

    def case_2():
        try:
            email_label = browser.find_element(By.ID, "email")
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", email_label)
            login("teste1@teste.com","Teste",browser)

            error_message = error_message_login(browser)
            assert "Authentication failed" in error_message.text.strip()
            print("Case 2 executed successfully.")

        except Exception as e:
            print(f"Error during Case 1: {e}")

    case_2()

finally:
    time.sleep(2)
    browser.quit()
