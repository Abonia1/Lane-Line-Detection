import opencv as cv2
import numpy as np

def canny(img):

gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
canny=cv2.Canny(blur,50,150)
return canny


image=cv2.imread('img.png')
lane_image=np.copy(image)
canny=canny(lane_image)
#cv2.imshow('result',gray)
cv2.imshow('result',canny)
cv2.waitKey(0)
# lane_image=np.copy(image)
# ghray=cv2.cvtColor()