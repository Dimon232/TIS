from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://auth.edimdoma.ru/login?service=https%3A%2F%2Fwww.edimdoma.ru%2Fusers%2Fservice')

try:
    username = browser.find_element(by=By.NAME, value='username')
    username.send_keys('dmorev17@mail.ru')
    
    password = browser.find_element(by=By.NAME, value='password')
    password.send_keys('qwerty')
    
    button = browser.find_element(by=By.NAME, value='button')
    button.click()
    print('The test was completed successfully')

except Exception as err:
    print('The test was failed')
    print(f'Error: {err}')

browser.quit()
