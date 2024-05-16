from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("https://www.edimdoma.ru/retsepty?with_ingredient=&with_ingredient_condition=and&without_ingredient=&user_ids=&field=&direction=&query=")

try:
    checkbox = browser.find_element(By.XPATH, '//input[@value="основные блюда"]')

    if not checkbox.is_selected():
        checkbox.click()

    show_button = browser.find_element(By.ID, 'recipe-filters-submit')
    show_button.click()
    print('The test was completed successfully')

except Exception as err:
    print('The test was failed')
    print(f'Error: {err}')

browser.quit()
