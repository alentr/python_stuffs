import io

import urllib3
from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb_image = Workbook()

ws_image = wb_image.active

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.worten.pt/i/5b1766f896c8145317ab0816e4f2f001f17114f4')
image_file = io.BytesIO(r.data)
img = Image(image_file)

img.width = 250
img.height = 190

ws_image.add_image(img, 'C5')
ws_image.row_dimensions[5].height = 145
ws_image.column_dimensions['C'].width = 34

wb_image.save("test_image.xlsx")
