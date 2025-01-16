from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome()

try:
     navegador.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
     navegador.maximize_window()

     def caso_3():  # Dado que o usuário tenta se cadastrar com e-mail incorreto
      WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "email_create")))
      navegador.find_element(By.ID, "email_create").send_keys("teste@teste")
      navegador.find_element(By.ID, "SubmitLogin").click()

     error_message = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.ID, "create_account_error"))
        )
     assert "Invalid email address." in error_message.text
     print(error_message.text)     

     caso_3()

finally:
    navegador.quit()