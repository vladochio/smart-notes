from PIL import Image, ImageFilter

with Image.open('зображення.jpg')as pic_original:
    pic_gray = pic_original.convert('L')
    contour = pic_original.filter(ImageFilter.CONTOUR)
    contour.save('countour.png')
    contour.show()

    
