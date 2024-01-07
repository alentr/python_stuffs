from datetime import datetime

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.worten.pt/promocoes')

wait_time_for_cookies = 5
print(f'{datetime.now()}: waiting {wait_time_for_cookies} seconds for cookies popup')
driver.implicitly_wait(wait_time_for_cookies)

try:
    # find for button to confirm cookies
    btn_cookie = driver.find_element(By.XPATH, '//*[@class="button--primary button--md button--black button"]')

    if btn_cookie is not None:
        btn_cookie.click()
except:
    print(f'{datetime.now()}: Button to confirm cookie was not found')

print(f'{datetime.now()}: instantiating xlsx')

workbook = openpyxl.Workbook()
workbook.remove(workbook['Sheet'])
workbook.create_sheet('Promoções')
sheet_products = workbook['Promoções']

sheet_products['A1'].value = 'Produto'
sheet_products['B1'].value = 'Preço'

print(f'{datetime.now()}: finding page size')
# pages = driver.find_element(By.XPATH, '//li[@class="numbers-pagination__number--last numbers-pagination__number--disabled numbers-pagination__number"]').text
pages = 2
print(f'{datetime.now()}: found {pages} pages')

products_on_sale = []

for i in range(1, int(pages) + 1):
    print(f'{datetime.now()}: getting products on sale at page number {i}')
    driver.get(f'https://www.worten.pt/promocoes?page={i}')
    products_on_sale = driver.find_elements(By.CLASS_NAME, 'product-card__text-container')
    print(f'{datetime.now()}: found {len(products_on_sale)} products on sale at page number {i}')

    print(f'{datetime.now()}: appending these products to the xlsx file')
    for prod_on_sale in products_on_sale:
        desc = prod_on_sale.find_element(By.XPATH, ".//span[@class='produc-card__name__link']").text
        price = prod_on_sale.find_element(By.XPATH, ".//span[@class='price__container']//span[@class='value']").text
        sheet_products.append([desc, price])

print(f'{datetime.now()}: all products were appended to the xlsx file')

xlsx_name = 'Promoções Worten.xlsx'
workbook.save(xlsx_name)
print(f'{datetime.now()}: {xlsx_name} file created')
print(f'{datetime.now()}: closing webdriver')
driver.quit()
