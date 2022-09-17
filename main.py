import qrcode
import sys

def usage():
    print(f"""
Usage: {sys.argv[0]} <URL> <image name>
    """)
if len(sys.argv) != 3:
    usage()
    sys.exit(1) 
input_data = sys.argv[1]
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='transparent')
img.save(sys.argv[2])
