### Lane-Line-Detection

### Gray the image:
Need to change rgb to gray scale and result will be as below:

![image](https://drive.google.com/uc?export=view&id=1ROZzZ8uJ-XlI27HMeeOQv521PskbtPE9)

### Blur the image 
Blur the image for too to feed to canny edge detection step and result will be as below:

![image](https://drive.google.com/uc?export=view&id=12wfFpUb4T50Cmq8OSy-tYw2DdxX8XDyV) 

### Canny edge detection
Sudden change in threshold of the image is called edge so here with tis step edge of the lane lines are found via this step and result will be as below:

![image](https://drive.google.com/uc?export=view&id=15AVVc7RlKTNK45cwS4OA0ErrCK_DTusq)


### Matplot 
To calculate and find the region of interest using x and y coordinates and result will be as below:

![image](https://drive.google.com/uc?export=view&id=1YkR9b98xVsuHtuwZeEtwjpIElh8ZygRv)

### Region of interest

once we found ROI then we must mask it with fillpoly function and result will be as below:

![image](https://drive.google.com/uc?export=view&id=1CrO3XBOO4b8AFf30WsgDv5PM8HZKcFyU)

### Bitwise And  to find the mask of the canny image

BitwiseAnd is calculated with bit value of each pixel value to get the cropped image of canny and result will be as below:

![image](https://drive.google.com/uc?export=view&id=1kgbHIrxr_oqmcPWGNPsgVh9F3lrTTaiv)


For calcuation and computation about image preprocessing and to play with pixel just visit the link

https://github.com/Abonia1/ComputerVision-AI/wiki


