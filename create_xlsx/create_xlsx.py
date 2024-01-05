import random
import openpyxl
from random_word import RandomWords

workbook = openpyxl.Workbook()
workbook.create_sheet('Products')
sheet_products = workbook['Products']

sheet_products['A1'].value = 'Name'
sheet_products['B1'].value = 'Price'

r = RandomWords()

for i in range(10):
    name = r.get_random_word()
    price = round(random.uniform(1, 10000), 2)
    sheet_products.append([name, price])

    print(name)
    print(price)

workbook.save('products.xlsx')
