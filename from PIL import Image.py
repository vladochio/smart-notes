from PIL import Image

with Image.open('зображення.jpg')as pic_original:
    print('зображення.jpg \n: Розмір', pic_original.size)
    print('Формат:', pic_original.format)
    print('Режим:', pic_original.mode)
    pic_original.show()
    