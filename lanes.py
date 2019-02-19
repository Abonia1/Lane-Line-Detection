import  cv2
import numpy as np
import matplotlib.pyplot as plt
def make_coordinates(image,line_parameters):
    slope,intercept=line_parameters
    #ex: y1=7704 and y2=422
    y1=image.shape[0]
    y2=int(y1*(3/5))
    #x=y-m/b
    x1=int ((y1-intercept)/slope)
    x2=int ((y2-intercept)/slope)
    return np.array([x1,y1,x2,y2])

def average_slope_intercept(image,lines):
    """left and right side lines"""
    left_fit=[]
    right_fit=[]
    if lines is not None:
        for line in lines:
            #print(line)
            #unpack array
            x1,y1,x2,y2=line.reshape(4)
            #polyfit fit the y=mx+b polynomial to x,y pts and return vec of co-efficients those gonna be vector of co-efficients  descripe slope of y intercept 
            parameter=np.polyfit((x1,x2),(y1,y2),1)
            slope=parameter[0]
            intercept=parameter[1]
            # when Y>X
            if slope <  0:
                left_fit.append((slope,intercept))
            else:
                right_fit.append((slope,intercept))
        #print(left_fit)
        #print(right_fit)
        left_fit_average=np.average(left_fit,axis=0)
        right_fit_average=np.average(right_fit,axis=0)
        left_line=make_coordinates(image,left_fit_average)
        right_line=make_coordinates(image,right_fit_average)
        return np.array([left_line,right_line])


def canny(image):

    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            #print(line)
            #unpack array
            x1,y1,x2,y2=line.reshape(4)
            """(x1,y1),(x2,y2) coordinate of line-color of line (255,0,0)-thickness of line 10"""
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image

def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([[(200,height),(1100,height),(550,250)]])
    mask=np.zeros_like(image)
    """to fill polygon with mask"""
    cv2.fillPoly(mask,polygons,255)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image

"""image=cv2.imread('img.png')
lane_image=np.copy(image)
canny=canny(lane_image)
cropped_image=region_of_interest(canny)

"2px is size of bin(1 is too small take long time)
1 degree of radian=np.pi(180)
threshold 100 
placehoder array
minlinelength is length of line pixel accepted 40 cause >40 is rejected
maxlinegab for line should be contionous and not broken "

lines=cv2.HoughLinesP(cropped_image,2,np.pi/(180),100,np.array([]),minLineLength=40,maxLineGap=5)
line_image=display_lines(lane_image,lines)
#apply lines in real image
combo_image=cv2.addWeighted(lane_image,0.8,line_image,1,1)
averaged_lines=average_slope_intercept(lane_image,lines)
line_image=display_lines(lane_image,averaged_lines)

cv2.imshow("result",combo_image)
cv2.waitKey(0)"""

# plt.imshow(canny)
# plt.show(0)

#cv2.imshow('result',gray)
#cv2.imshow('result',canny)
"""cv2.imshow("result",region_of_interest(canny))
cv2.waitKey(0)"""
# lane_image=np.copy(image)
# ghray=cv2.cvtColor()



cap=cv2.VideoCapture("test.mp4")
while(cap.isOpened()) :
    _,frame=cap.read()
    canny_image=canny(frame)
    cropped_image=region_of_interest(canny_image)
    lines=cv2.HoughLinesP(cropped_image,2,np.pi/(180),100,np.array([]),minLineLength=40,maxLineGap=5)
    averaged_lines=average_slope_intercept(frame,lines)
    line_image=display_lines(frame,averaged_lines)
    combo_image=cv2.addWeighted(frame,0.8,line_image,1,1)
    cv2.imshow("result",combo_image)
    if cv2.waitKey(1)  & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

