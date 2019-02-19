import  cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):

    gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def display_lines(image,lines):
    lane_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            print(line)

def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([[(200,height),(1100,height),(550,250)]])
    mask=np.zeros_like(image)
    """to fill polygon with mask"""
    cv2.fillPoly(mask,polygons,255)
    masked_image=cv2.bitwise_and(canny,mask)
    return masked_image

image=cv2.imread('img.png')
lane_image=np.copy(image)
canny=canny(lane_image)
cropped_image=region_of_interest(canny)

"""2px is size of bin(1 is too small take long time)
1 degree of radian=np.pi(180)
threshold 100 
placehoder array
minlinelength is length of line pixel accepted 40 cause >40 is rejected
maxlinegab for line should be contionous and not broken 
"""
lines=cv2.HoughLinesP(cropped_image,2,np.pi/(180),100,np.array([]),minLineLength=40,maxLineGap=5)
line_image=display_lines(lane_image,lines)

cv2.imshow("result",lines)
cv2.waitKey(0)

# plt.imshow(canny)
# plt.show(0)

#cv2.imshow('result',gray)
#cv2.imshow('result',canny)
"""cv2.imshow("result",region_of_interest(canny))
cv2.waitKey(0)"""
# lane_image=np.copy(image)
# ghray=cv2.cvtColor()