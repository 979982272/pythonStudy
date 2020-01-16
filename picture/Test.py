from PIL import Image
import pytesseract
text=pytesseract.image_to_string(Image.open('c:\\s.jpg'),lang='chi_sim')
print(text)