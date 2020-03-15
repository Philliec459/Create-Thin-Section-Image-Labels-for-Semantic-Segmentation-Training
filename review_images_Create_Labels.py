# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:41:41 2020

@author: craig
"""

from PIL import Image
import os.path


#import skimage
from skimage.color import rgb2gray
from skimage.filters import sobel, gaussian, hessian, frangi, laplace, median  
#    meijering, prewitt, prewitt_h, prewitt_v, sato

import numpy as np
import matplotlib.pyplot as plt



'''
    Read in all Thin Section Images and Create Labels scaled 1 to 5
'''
for i in range(1,13,1):   

    TS=str(i)

    img=os.path.join('ClasticThinSections', TS + '.png')

    TS_Im = Image.open(img)
    
    data = np.array(TS_Im) 


    '''
        Create Gray Level Images from which we wull threshold for our sgement labels
    '''
    #gradient = np.array(TS_Im)
    #gradient = sobel(rgb2gray(data))  # true gradients
    gradient = gaussian(rgb2gray(data)) #averagint
    #gradient = median(rgb2gray(data)) #average this is best for thin sections scaled 0 to 256
    #gradient = hessian(rgb2gray(data)) # picks out grains
    #gradient = frangi(rgb2gray(data)) # really weird 
    #gradient = laplace(rgb2gray(data)) # creates higher grains and lower matrix extremely well 
    #gradient = meijering(rgb2gray(data)) #shows paths ofpossible flow????
    #gradient = prewitt(rgb2gray(data)) #gradient like sobel
    #gradient = sobel(rgb2gray(data))  # true gradients
    #gradient = prewitt_h(rgb2gray(data)) #creates higher grains and lower matrix extremely well 
    #gradient = prewitt_v(rgb2gray(data)) #creates higher grains and lower matrix extremely well with vertical bias
    #gradient = sato(rgb2gray(data)) #weidrd like frangi
    
    
    '''
        Create Labels scaled 1 to 5
    '''

    label = np.zeros(gradient.shape )

    label[gradient < 0.25] = 1 #black grains 
    label[gradient > 0.25] = 2 #blue dye epoxy 
    label[gradient > 0.4]  = 3 #darker grains- dark orange   
    label[gradient > 0.6]  = 4 #darker portions of bright grain, edges - orange  
    label[gradient > 0.8]  = 5 #bright grains - Yellow   


    '''
        Save label images scaled segment 1 to segment 5
    '''
    
#    ##### for images scaled 0 to 1
#    img_out=os.path.join('ClasticThinSectionsLabels', TS + '.png')
#    imsave(img_out,label)
    
    ##### for images 0 to 255
    img_out=os.path.join('ClasticThinSectionsLabels', TS + '.png')    
    im = Image.fromarray(label)
    im = im.convert("L")       
    im.save(img_out)



    '''
        Plot data
    '''
    plt.figure(0)
    plt.imshow(data)  #Original Thin Section Image

    plt.figure(1)    
    histogram, bin_edges = np.histogram(data, bins=256, range=(0.0, 254))   
    plt.title(" Histogram Original Thin Section Image")
    plt.xlabel(" value")
    plt.ylabel("pixels")  
    plt.plot(bin_edges[0:-1], histogram)  # <- or here



    plt.figure(2)
    plt.imshow(gradient)  #Gradient Gray Level Image

    plt.figure(3)    
    histogram, bin_edges = np.histogram(gradient, bins=256, range=(0.0, 1))   
    plt.title(" Histogram Gradient Gray-Level Image")
    plt.xlabel(" value")
    plt.ylabel("pixels")  
    plt.plot(bin_edges[0:-1], histogram)  # <- or here




    plt.figure(5)
    plt.imshow(label)  #Labeled Image
    
    plt.figure(6) 
    histogram, bin_edges = np.histogram(label, bins=256, range=(0.0, 6))   
    plt.title(" Histogram of Labeled Image")
    plt.xlabel(" value")
    plt.ylabel("pixels")  
    plt.plot(bin_edges[0:-1], histogram)  # <- or here

    
 
