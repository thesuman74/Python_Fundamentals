import qrcode

def generate_qr_code():
    # Ask the user for data to encode
    data = input("Enter the data to encode in the QR code: ")

    # Create an instance of the QRCode class
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # Add data to the instance 'qr'
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color='black', back_color='white')

    # Save the QR code image
    img.save('QRcode.png')

    print("QR code generated successfully!")

if __name__ == "__main__":
    generate_qr_code()
