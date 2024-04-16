from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configurações do WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximiza a janela do navegador
driver = webdriver.Chrome(options=chrome_options)

# Abrir o site em uma nova aba
driver.execute_script("window.open('https://www.rpachallenge.com/', '_blank')")
driver.switch_to.window(driver.window_handles[1])

# Esperar até que o elemento seja carregado na página
FirstName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]')
FirstName.send_keys("Achilles")

LastName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]')
LastName.send_keys("Guilardi")

LastAddress = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]')
LastAddress.send_keys("Rua Nove")

Email = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]')
Email.send_keys("Rua Nove")

CompanyName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]')
CompanyName.send_keys("Domvs IT")

Phone = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]')
Phone.send_keys("123456789")

Role = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]')
Role.send_keys("São Paulo - Brazil")

time.sleep(15)

BotaoSubmit = driver.find_element(By.CSS_SELECTOR, '[class="btn uiColorButton"]')
BotaoSubmit.click()

# Aguardar 60 segundos
time.sleep(15)
