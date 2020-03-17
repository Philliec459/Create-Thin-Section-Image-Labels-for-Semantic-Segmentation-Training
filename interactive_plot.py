#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:37:19 2020

@author: craig
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageOps 
import os.path
from skimage.color import rgb2gray,gray2rgb
from skimage.filters import sobel,gaussian,hessian,frangi,laplace,median
#meijering, prewitt, prewitt_h, prewitt_v, sato
from skimage.io import imsave

'''
# =============================================================================
# Drive this from terminal window
# =============================================================================
'''
img_label = cv2.imread('3.png')
#img = Image.open('sample_images/1_output.png')

data = np.array(img_label) 

#data = np.around(rgb2gray(data_original)*100) #averagint
#data =np.around(gaussian(rgb2gray(data_original)*100)) #averagint
#data =np.around(median(rgb2gray(data_original)*1)) #averagint

#import mpldatacursor
from mpldatacursor import datacursor

fig, ax = plt.subplots()
ax.imshow(data, interpolation='none')
#mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))
datacursor(display='single')
plt.show()


#
#
#label = np.zeros(data.shape )
##label[data ==68] = 68  #walls
##label[data ==54] = 54 #window with no drapes
##
##label[data >2] = 86 #well defined edges of each segment using sobel filter
#
##label[data ==80] = 80 #rug
##label[data ==56] = 56 #table
##label[data ==77] = 77 #edge of pillows
##label[data ==18] = 18 #pillows
#label[data ==61]  = 61 #bed
##label[data ==52]  = 52 #ceiling
##label[data ==33]  = 33 #floor and dark parts
##label[data ==68]  = 68 #fchandalier
##label[data ==77]  = 77 #windows with drapes
##label[data ==59]  = 59 #lamps
##label[data ==20]  = 20 #back wall dresser
##label[data ==56]  = 56 #plant in corner
#
#
###mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))
##datacursor(display='single')
##
##plt.show()
#
#
#
#    
###### for images 0 to whatever
#img_out=os.path.join('segs/' + 'bed_labels.png')
#
#im = Image.fromarray(label)
#im = im.convert("L")
#im.save(img_out) 
#
#
#
#
##########im_new = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
#
#'''
#    This is the Green Box 
#'''
#
#pic = cv2.imread(img_out)
#img = cv2.pyrDown(pic)
#
#
## threshold image
##ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
##                127, 255, cv2.THRESH_BINARY)
#ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
#                30, 255, cv2.THRESH_BINARY)
#
##ret, threshed_img = cv2.threshold(img,127, 255, cv2.THRESH_BINARY)
#
#
## find contours and get the external one
#contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
##image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
##                cv2.CHAIN_APPROX_SIMPLE)
## with each contour, draw boundingRect in green
## a minAreaRect in red and
## a minEnclosingCircle in blue
#for c in contours:
#    # get the bounding rect
#    x, y, w, h = cv2.boundingRect(c)
#
#    '''
#    # draw a green rectangle to visualize the bounding rect
#    '''
#    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#
#    # get the min area rect
#    rect = cv2.minAreaRect(c)
#    box = cv2.boxPoints(rect)
#    # convert all coordinates floating point values to int
#    box = np.int0(box)
#
#
#
##    '''
##    # draw a red 'nghien' rectangle
##    '''
##    cv2.drawContours(img, [box], 0, (0, 0, 255))
#
#
#
##    '''
##    # finally, get the min enclosing circle
##    '''
##    (x, y), radius = cv2.minEnclosingCircle(c)
##    # convert all values to int
##    center = (int(x), int(y))
##    radius = int(radius)
##    # and draw the circle in blue
##    img = cv2.circle(img, center, radius, (255, 0, 0), 2)
#
#
#
#print(len(contours))
#cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
#cv2.imshow("Hit Esc to exit", img)
#cv2.imshow("Hit Esc to exit", img)
#
#
#'''
#     **** use Esc to get out ****
#'''
#while True:
#    key = cv2.waitKey(1)
#    if key == 27: #ESC key to break
#        break
#
#cv2.destroyAllWindows()
#
#img_out3=os.path.join('segs/' + 'bed_labels_box.png')
#img = cv2.pyrUp(cv2.drawContours(img, contours, -1, (255, 255, 0), 1))
#imsave(img_out3,img)