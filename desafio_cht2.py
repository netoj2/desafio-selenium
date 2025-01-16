from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
mobile_emulation = {
    "deviceName": "iPhone X"
}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
   
navegador = webdriver.Chrome(options=chrome_options)

try:
    
    navegador.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

    def caso_2(): #Dado que o usuário tenta logar com credenciais incorretas - mobile
        email_label = navegador.find_element(By.ID, "email")

        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", email_label)
        email_label.send_keys("teste@teste.com")
        navegador.find_element(By.ID, "passwd").send_keys("teste1")
        navegador.find_element(By.ID, "SubmitLogin").click()
        print("Caso 2 executado com sucesso.")
 

    caso_2()

finally:
    time.sleep(5)
    navegador.quit()
