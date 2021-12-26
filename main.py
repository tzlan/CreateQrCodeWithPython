from qrcode.main import QRCode
from qrcode.main import make  # noqa
from qrcode.constants import (  # noqa
    ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H)

from qrcode import image  # noqa


def run_example(data="https://www.youtube.com/channel/UCtojr-ULCp1Y6RSwQtaM6HQ", *args, **kwargs):

    qr = QRCode(*args, **kwargs)
    qr.add_data(data)

    im = qr.make_image()
    im.show()


if __name__ == '__main__':  # pragma: no cover
    import sys
    run_example(*sys.argv[1:])


qr = QRCode(

    version = 1,
    box_size=50,
    border =2
)

myurl = 'https://www.youtube.com/channel/UCtojr-ULCp1Y6RSwQtaM6HQ'

qr.add_data(myurl)
qr.make(fit=True)

img = qr.make_image(fill_color = "black" , back_color="white")
img.save('output.png')