# Create-Labels-for-Thin-Sections
Create Labels for image-segmentation:

This is meant to document the steps being used to create a labeled image for the image segmentation using Keras per Divam Gupta's GitHub repository. 

We are trying to label different types of grains or blue dye epoxy (this represents visual porosity) observed in clastic petrographic thin sections. The following image is an example of a typical clastic thin section that we are working with for our test data:

![Image](ThinSection.png)

We read in the original Thin Section image and create a Numpy array. 

    TS_Im = Image.open(img)
    
    data = np.array(TS_Im) 

We then convert the color image to a gray-level image using the following code:

    gradient = gaussian(rgb2gray(data)) 

using skimage filter gaussian (or median) filters and skimage rgb2gray. 

The following is an example of the gray-level image and histogram of these data scaled 0 to 1.  

![Image](GradientThinSection.png)

We then partition the gray-level image data into different bins which will serve as our labels:

 
    label = np.zeros(gradient.shape )

    label[gradient < 0.25] = 1 #black grains 
    label[gradient > 0.25] = 2 #blue dye epoxy 
    label[gradient > 0.4]  = 3 #darker grains- dark orange   
    label[gradient > 0.6]  = 4 #darker portions of bright grain, edges - orange  
    label[gradient > 0.8]  = 5 #bright grains - Yellow   


We are scaling our label data from 1 to 5 to represent the segments in the image that will be used as annotated labels for our image segmentation training. 


![Image](LabelThinSection.png)

The histogram verifies that we have 5 labels in our saved images.


