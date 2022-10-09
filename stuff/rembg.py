import cv2
import numpy as np
from PIL import Image
'''
img = Image.open('signature.jpg')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        if item[0] > 150:
            newData.append((0, 0, 0, 255))
        else:
            newData.append(item)

img.putdata(newData)
img.save('signature_trans.png', 'PNG')

#img = Image.open('signature_trans.png')  
#img.show()
'''

# median blur, adaptive, gaussian, inv, dilation 5,5
img = cv2.imread('signature.jpg', 0)
img = cv2.resize(img, (480, 200))
#canny = cv2.Canny(img, 100, 250)
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
blur = cv2.GaussianBlur(img, (7,7), 0)

kernel = np.ones((1,1), np.uint8)
#blur = cv2.dilate(img, kernel, iterations = 1)
cv2.imshow('edge', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
