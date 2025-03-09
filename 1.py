from PIL import Image

with Image.open('зображення.jpg')as pic_original:
    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    pic_gray.show()