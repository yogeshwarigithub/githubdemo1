import pyqrcode
url="https://www.w3schools.com/MySQL/default.asp"
k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)