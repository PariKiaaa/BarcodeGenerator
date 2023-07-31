from datetime import datetime
from PIL import Image
import barcode 
from barcode import EAN13
from barcode.writer import ImageWriter

# Function to generate a filename based on the current date and time or a custom name if provided.
def FileName(customize=''):
    if customize:
        return customize
    else:
        now = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        return now

# Function to generate a barcode for a numeric input (EAN-13 barcode).
def NumberBarcode(number):
    name = FileName()  # Generate a unique filename

    with open(f'{name}.png', 'wb') as f:  # Create the PNG file to store the barcode image
        EAN13(str(number), writer=ImageWriter()).write(f)  # Create the EAN-13 barcode using the given number
        img = Image.open(f"{name}.png")  # Open the generated barcode image
        img.show()  # Display the barcode image

# Function to generate a barcode for any given text input and barcode type.
# By default, it uses the 'code128' type which supports both numbers and alphabets.
def AnyBarcode(text, Type='code128'):
    name = FileName()  # Generate a unique filename

    BarcodeType = barcode.get_barcode_class(Type)  # Set the desired barcode type
    image = BarcodeType(text, writer=ImageWriter())  # Create the barcode using the given text and type
    image.save(name)  # Save the generated barcode image to a file

    img = Image.open(f"{name}.png")  # Open the generated barcode image
    img.show()  # Display the barcode image

# Example: Generate and display a barcode for the given text 'Pardis Kiaeifar' using the default 'code128' type.
AnyBarcode('PariKia')

# Example: Generate and display an EAN-13 barcode for the given number '1001234567890'.
NumberBarcode('1001234567890')
