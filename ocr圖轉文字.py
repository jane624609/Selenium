#OCR辨識圖片為文字
#準備工作:用系統管理員身分在com下 pip install pillow 以及 pip install pytesseract

#完成上述步驟會遇到异常如下:pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your path
#检查上述报错中的pytesseract.py源码，发现如下说明：
  # CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
  #tesseract_cmd = 'tesseract'

#到下面的網址下載並安裝 tesseract OCR:https://github.com/UB-Mannheim/tesseract/wiki
#安裝好後找到 pytesseract.exe 的位置，並複製其絕對路徑，通常會在 C:\Program Files\Tesseract-OCR\tesseract.exe。
#然后将源码pytesseract.py中的：tesseract_cmd = 'tesseract'更改为：tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

import pytesseract

img = Image.open('4.png')
text = pytesseract.image_to_string(img, lang='chi_tra+eng') #OCR辨識 英文:lang="eng" /繁體中文:lang="chi_tra" /中文與英文:lang="chi_tra+eng"
print(text)


#教學https://ithelp.ithome.com.tw/articles/10227263