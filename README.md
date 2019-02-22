### Lane-Line-Detection

### Image File
Initial image file is available [here](https://github.com/Abonia1/Lane-Line-Detection/blob/master/img.jpg)

### Gray the image
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

### Hough Transform

Maximum number of intersection inside bin


### Line computation
line s 2D array with 1 row and 2 cols
[[704 418 927 641]]
[[704 426 791 516]]
[[320 703 445 494]]
[[585 301 663 381]]
[[630 341 670 383]]
[[794 520 861 591]]
[[659 371 704 416]]
[[870 599 939 672]]
[[767 493 807 534]]
[[423 509 454 461]]
[[940 653 991 702]]
[[824 551 879 609]]
[[676 389 754 467]]

### Display Lines
Display line method make image to black 
Find coordinates of each line 
Apply this coordinate to lines in black image

 and result will be as follow:note(I have mentioned B with high value and make RG as 0)
 
![image](https://drive.google.com/uc?export=view&id=1ba9wTARYmCHSLPo0LPrluW0QD0S5wJBn)
 
 also finally apply lines in real image as follow:
 
 ![image](https://drive.google.com/uc?export=view&id=1c5n6fFGTzKpwmnkZi7IzpycFj0YYu9NM)
 
 
###  Averaging  the lines

Averaged line to find a smooth line for clear detection and result as below:

![image](https://drive.google.com/uc?export=view&id=1g_YfiFAr5feZWLIM0Fjk2s4xEfyYd4C9)


Average lineintegration with combo image and result as below:

![image](https://drive.google.com/uc?export=view&id=13XY6ZMT134wwtW9ZJ3PjV9HldlJemslH)


### Adding input as video frame 

The video file to be feed is [test.mp4](https://github.com/Abonia1/Lane-Line-Detection/blob/master/test.mp4)



### Test Drive video

I have tested with best parameter and model in driving env act as in video file [testDrive.mp4](https://github.com/Abonia1/Lane-Line-Detection/blob/master/testDrive.mp4)

For calcuation and computation about image preprocessing and to play with pixel just visit the link

https://github.com/Abonia1/ComputerVision-AI/wiki


