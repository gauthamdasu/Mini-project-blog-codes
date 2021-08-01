from pyqrcode import create
import png


def embed_QR(url_input, location_name):
    embedded_qr = create(url_input)
    embedded_qr.png(location_name, scale=7)
