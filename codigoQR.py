import qrcode
# Link for website
input_data = "https://dev.azure.com/vguerraz/TraceFood/_wiki/wikis/TraceFood.wiki/29/Entregable-2"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=60,
        border=2)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode002.png')