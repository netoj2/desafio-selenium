from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


navegador = webdriver.Chrome()

try:
    navegador.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
    navegador.maximize_window()

    def caso_1(): #Dado que o usuário tenta logar com credenciais incorretas - web
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "email")))
        navegador.find_element(By.ID, "email").send_keys("teste@teste.com")
        navegador.find_element(By.ID, "passwd").send_keys("teste1")
        navegador.find_element(By.ID, "SubmitLogin").click()

        error_message = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
        )
        assert "Authentication failed" in error_message.text
        print("Caso 1 executado com sucesso.")

    caso_1()

finally:
    navegador.quit()