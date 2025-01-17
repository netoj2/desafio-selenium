from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setup import init_setup
import time

browser = init_setup(mobile=False)

try:

    def case_3():  # Dado que o usuário tenta se cadastrar com e-mail incorreto
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "email_create")))
        browser.find_element(By.ID, "email_create").send_keys("teste@teste")
        browser.find_element(By.NAME, "SubmitCreate").click()

        error_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#create_account_error ol li"))
        )
        assert "Invalid email address." in error_element.text

    case_3()
    print("Case 3 executed successfully")

finally:
    time.sleep(2)
    browser.quit()