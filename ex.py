import os 
#os.chdir('')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#q1
image = mpimg.imread('stade.bmp')
plt.imshow(image)

#q2
long_img = image.shape[1]
larg_img = image.shape[0]
print( 'long * larg : ', long_img * larg_img)

#q3
def coul(image):
        coul_ter = image[int(long_img/2+2),int(larg_img/2)]
        return coul_ter 

#q5
def maillot():
        coul1 = coul(image)
        coul2 = [255, 255, 255]
        return [coul1, coul2]



plt.show()