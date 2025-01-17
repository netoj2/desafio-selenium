from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_setup(mobile = False):
    if(mobile):
        chrome_options = Options()
        mobile_emulation = {
            "deviceName": "iPhone X"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        browser = webdriver.Chrome(options=chrome_options) 
        browser.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        return browser
      
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
    browser.maximize_window()
    return browser

def login(email, senha, browser):
    browser.find_element(By.ID, "email").send_keys(email)
    browser.find_element(By.ID, "passwd").send_keys(senha)
    browser.find_element(By.ID, "SubmitLogin").click()

def error_message_login(browser):
    return WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
    )
