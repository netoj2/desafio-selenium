from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

# Dado que o usuário tenta logar com credenciais incorretas
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("naoexiste@email.com")
password_field = driver.find_element(By.ID, "passwd")
password_field.send_keys("senhaerrada")
driver.find_element(By.ID, "SubmitLogin").click()

# Então o sistema exibe a mensagem de erro
error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
assert "Authentication failed" in error_message.text

time.sleep(5)
driver.quit()

###########
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")


# Dado que o usuário tem credenciais válidas
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("usuario_valido@email.com")
password_field = driver.find_element(By.ID, "passwd")
password_field.send_keys("senha_valida")
driver.find_element(By.ID, "SubmitLogin").click()

# Adicionando espera explícita para garantir que o redirecionamento aconteça
WebDriverWait(driver, 10).until(
    EC.url_contains("controller=my-account")
)

# Então o sistema redireciona o usuário para "My Account"
assert "controller=my-account" in driver.current_url

time.sleep(5)
driver.quit()

##########
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

# Dado que o usuário tenta se cadastrar com um e-mail inválido
email_field = driver.find_element(By.ID, "email_create")
email_field.send_keys("email_invalido.com")
driver.find_element(By.ID, "SubmitCreate").click()

# Então o sistema exibe a mensagem de erro para e-mail inválido
error_message = driver.find_element(By.ID, "create_account_error")
assert "Invalid email address" in error_message.text

time.sleep(5)
driver.quit()