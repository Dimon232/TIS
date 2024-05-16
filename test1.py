from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://www.edimdoma.ru/retsepty?tags%5Brecipe_jv%5D%5B%5D=%D0%92%D1%81%D0%B5+%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1%8B&with_ingredient=&with_ingredient_condition=and&without_ingredient=&user_ids=&field=&direction=&query=')

try:
    query_input = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'query')))

    query_input.send_keys('Тестовый запрос')

    submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.field__button')))

    submit_button.click()
    print('The test was completed successfully')

except Exception as err:
    print('The test was failed')
    print(f'Error: {err}')

browser.quit()
