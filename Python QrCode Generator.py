import qrcode

link=input('Enter your URL: ').strip()
file_name=input('Enter the name you want to give to the file: ').strip()
qr_code=qrcode.QRCode(box_size=10, border=4)
qr_code.add_data(link)
image=qr_code.make_image(fill_color='black', back_color='white')
image.save(file_name)
print(f'QR code saved as {file_name}')