from tesserocr import PyTessBaseAPI
from PIL import Image

api = PyTessBaseAPI(lang='script/Thai')
api.SetImage(Image.open("sample/thaiid.jpeg"))
# api.SetImage(Image.open("sample/thaiid.jpeg"))
print(api.GetUTF8Text())

