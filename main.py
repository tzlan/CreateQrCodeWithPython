import qrcode

qr = qrcode.QRCode(

    version = 1,
    box_size=50,
    border =2
)

myurl = 'https://www.youtube.com/channel/UCtojr-ULCp1Y6RSwQtaM6HQ'

qr.add_data(myurl)
qr.make(fit=True)

img = qr.make_image(fill_color = "black" , back_color="white")
img.save('output.png')