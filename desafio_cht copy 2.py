from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuração do ChromeDriver com emulação mobile
service = ("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
chrome_options = Options()

mobile_emulation = {
    "deviceName": "iPhone X"
}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

try:
    navegador = webdriver.Chrome(options=chrome_options).get(service)
    # navegador.maximize_window()

    def caso_1(): #Dado que o usuário tenta logar com credenciais incorretas
        email_label = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        navegador.execute_script("arguments[0].scrollIntoView(true);", email_label)
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "email")))
        email_label.send_keys("teste@teste.com")
        navegador.find_element(By.ID, "passwd").send_keys("teste1")
        navegador.find_element(By.ID, "SubmitLogin").click()

        error_message = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
        )
        assert "Authentication failed" in error_message.text
        print("Caso 1 executado com sucesso.")

    def caso_2(): # Dado que o usuário tenta logar com e-mail vazio
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "email")))
        email_field = navegador.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(" ")
        navegador.find_element(By.ID, "SubmitLogin").click()

        error_message = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
        )
        assert "An email address required." in error_message.text
        print("Caso 2 executado com sucesso.")

    caso_1()
    caso_2()

finally:
    navegador.quit()