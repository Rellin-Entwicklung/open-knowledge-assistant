import cv2
import pytesseract
from pytesseract import Output

try:
    print("version: ", pytesseract.get_tesseract_version[1])
except:
    print("Fehler")


img = cv2.imread('screen-test07.png')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
#d = pytesseract.image_to_data(img, output_type=Output.DICT)
#print(d.keys())

#custom_config = r'--oem 3 --psm 6'
#pytesseract.image_to_string(img, config=custom_config)



try:
    print("1", pytesseract.image_to_string('screen-test07.png', timeout=5)) # Timeout after 2 seconds
    #print("2:", pytesseract.image_to_string('screen-test04.png', timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    print("timout")
    pass

liste= pytesseract.image_to_string('screen-test07.png', timeout=5)
ergebnis = liste.split(' ')
print("ergebnis: ", ergebnis)
for number in ergebnis:
    print(number)



cv2.waitKey(0)