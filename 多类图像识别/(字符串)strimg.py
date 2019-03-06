from PIL import Image,ImageEnhance
import pytesseract

# text = pytesseract.image_to_string(Image.open("./pic/pythontest.png"))
# print(text)
text = pytesseract.image_to_string(Image.open("./pic/pythontest.png"))
print(text)
# text = pytesseract.image_to_string(Image.open("./pic/vv_3.png"))
# print(text)
# def test(value = 's3'):
#     print("第一圈试%s"%value)
# test(value = 's6')

def pic_dispose(x):
    # x = "./pic/mebx_test2.bmp"
    image = Image.open(x)
    image.show()
    #亮度
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.8
    image_brightened = enh_bri.enhance(brightness)
    image_brightened.show()
    #色感
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    image_colored.show()

    # 对比度增强
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()

    # 锐度增强
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()
# pic_dispose("./pic/mebx_test2.bmp")

im = Image.open('./pic/pythontest.png')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
im.show()
# 把缩放后的图像用jpeg格式保存:
# im.save('/Users/michael/thumbnail.jpg', 'jpeg')