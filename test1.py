from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Получаем в переменную browser указатель на браузер
browser = webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://auth.edimdoma.ru/login?service=https%3A%2F%2Fwww.edimdoma.ru%2Fusers%2Fservice')

# заполняем поле логин, привязываемся к элементу через его имя
username = browser.find_element(by=By.NAME, value='username')
username.send_keys('testtest')

# заполняем поле пароля, привязываемся к элементу через его id
password = browser.find_element(by=By.NAME, value='password')
password.send_keys('testtest')

# Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
button = browser.find_element(by=By.NAME, value='button')
# Нажимаем на кнопку входа
button.click()
# Проверка результата

try:
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

# Закрываем браузер
