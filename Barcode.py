from datetime import datetime
from PIL import Image
import barcode 
from barcode import EAN13
from barcode.writer import ImageWriter
#this module also uses PIL module as default

#Print all barcode types:
#print(barcode.PROVIDED_BARCODES)


def FileName(customize=''):  #sets the file name (date and time as default name)
	if customize:
		return customize
	else:
		now = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
		return now  #returns the date and time as a string


def NumberBarcode(number):  #only numbers
	name = FileName()

	with open(f'{name}.png','wb') as f:  #creating the jpg file as write binary
		EAN13(str(number),writer=ImageWriter()).write(f) #creare the barcode in EAN13 class (first arg=the number)
		img = Image.open(f"{name}.png")
		img.show()


#this function is more flexable ()
#you can change the barcodetype easily by giving the name of
#any barcode class as the second arg. it is code128 as default
#it is used for both numbers and alphabets, but its lenght is not always the best
def AnyBarcode(text,Type = 'code128'):
	name = FileName()

	BarcodeType = barcode.get_barcode_class(Type) #set the barcode type as code128 or anything else
	image = BarcodeType(text, writer=ImageWriter()) #creating the barcode (first arg=the text)
	image.save(name) #creates the file (arg = file name)

	img = Image.open(f"{name}.png")
	img.show()


#run:
AnyBarcode('Pardis Kiaeifar')
NumberBarcode('1001234567890')


#try this updates:
# set a default directory (like in another folder) and changeable
# use tkinter and make the client enter the text without seeing the source code