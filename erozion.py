from PIL import Image, ImageFilter, ImageOps
import cv2
 
filename = "test.bmp"

porog = 120

img_logo = Image.open(filename)
img_logo = img_logo.convert("L")
img_logo = img_logo.point(lambda x: 255 if x > porog else 0)
img_logo = img_logo.filter(ImageFilter.CONTOUR)
# img_logo = img_logo.filter(ImageFilter.MaxFilter(3))
img_logo = img_logo.filter(ImageFilter.MinFilter(1))
img_logo = img_logo.filter(ImageFilter.MinFilter(3))
# img_logo = img_logo.filter(ImageFilter.FIND_EDGES)
img_logo.show()
img_logo.save('1.png')
img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)
img_logo.show()
img_logo.save('2.png')