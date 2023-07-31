# Barcode Generator

## Description

This is a Python script that allows you to generate barcodes for numeric values and text inputs. The script uses the `barcode` and `PIL` (Python Imaging Library) libraries to create and display barcode images. The barcodes generated can be saved as PNG files.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- barcode
- PIL

You can install the required libraries using pip:

pip install barcode[pillow]

## Usage

1. Clone the repository or download the Python script `Barcode.py` and run the code.

2. To generate a barcode for a numeric value (EAN-13 barcode), use the NumberBarcode function:

NumberBarcode('1001234567890')

This will generate and display an EAN-13 barcode for the provided number '1001234567890'.

4. To generate a barcode for any text input and barcode type, use the AnyBarcode function:

AnyBarcode('PariKia', Type='code128')

This will generate and display a barcode for the given text 'PariKia' using the 'code128' barcode type (which supports both numbers and alphabets).

Note: You can customize the barcode type by providing the appropriate type as the Type parameter in the AnyBarcode function.

Feel free to use and modify this script according to your needs. Happy coding!
