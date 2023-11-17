# QRCodeGenerator
This Python program generates a QR code for a specified data input using the qrcode library. The Pillow (PIL) library is used to create and display the QR code image. The generated QR code is saved with a filename based on the current date and time unless a custom name is provided.

## Requirements
- Python 3.x
- Pillow library (install with: `pip install Pillow`)
- qrcode library (install with: `pip install qrcode`)

## Usage
1. Ensure that the required libraries are installed.
2. Run the program by executing the script (python QRCodeGenerator.py).
3. The program generates a QR code for the specified data (for example, 'google.com').
4. The generated QR code image is displayed, and a PNG file is saved with a filename based on the current date and time.

## Functionality
- The program generates a QR code with specified data.
- The QR code is displayed using the Pillow library.
- The generated QR code image is saved with a filename based on the current date and time, or a custom name if provided.

## Customizing Filename
- To customize the filename, provide a string when calling the `FileName` function. For example: `FileName('custom_name')`.
- If no custom name is provided, the filename will be based on the current date and time.

**Note:** Ensure that the specified data is compatible with QR code standards.
