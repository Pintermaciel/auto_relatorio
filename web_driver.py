import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#abrir pagina
driver.get('https://supre.nexello.com.br/v2/login')
time.sleep(2)

#login

username = driver.find_element_by_css_selector('#mat-input-1')
password = driver.find_element_by_css_selector('#mat-input-0')

time.sleep(5)

username.send_keys("matheuspinter")
password.send_keys("25130186")

time.sleep(2)

login = driver.find_element_by_class_name("mat-button-wrapper")
login.click()

time.sleep(20)

#buscar relatorio

