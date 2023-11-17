# Import necessary modules
from datetime import datetime
from PIL import Image
import qrcode

# Function to generate a filename based on the current date and time or a custom name if provided.
def FileName(customize=''):
    if customize:
        return customize
    else:
        now = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        return now
    
def generate(data):
    # Create a QRCode instance with specified version, box size, and border
    qr = qrcode.QRCode(
        version= 1,
        box_size = 15,
        border = 15
    )

    # Add data to the QR code instance and make it fit
    qr.add_data(data)
    qr.make(fit=True)
    
    # Make the QR code image with specified fill and back color
    img = qr.make_image(fill='black', back_color='white')

    # Generate a filename
    name = FileName()

    # Save the QR code image with the generated filename
    img.save(f'{name}.png')

    # Open the generated barcode image
    image = Image.open(f"{name}.png")
    
    # Display the generated QR code image
    image.show() 

# Example data
data = 'google.com'
# Generate QR code for the example data
generate(data)
