from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setup import init_setup, login, error_message_login
import time

browser = init_setup(mobile=True)

try:

    def case_2(): #Dado que o usuário tenta logar com credenciais incorretas - mobile
        email_label = browser.find_element(By.ID, "email")
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", email_label)
        login("teste1@teste.com","Teste",browser)

        error_message = error_message_login(browser)
        assert "Authentication failed" in error_message.text.strip()

    case_2()
    print("Case 2 executed successfully.")

finally:
    time.sleep(2)
    browser.quit()
