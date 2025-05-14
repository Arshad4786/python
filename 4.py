# import matplotlib.pyplot as plt
# from skimage import color,io

# image = io.imread("https://picsum.photos/200/300")

# gray = color.rgb2gray(image)

# plt.imshow(gray,cmap='gray')
# plt.axis('off')
# plt.show()

import numpy as np
arr = np.arange(1,21)
print(arr)
print(arr[::-1]) #slicing

arr1 = np.linspace(0,1,6)
print(arr1) # evenly spaced 6 values from 0 to 1


x= np.random.randint(0,10,size=(4,4))
print(x)
print(x.flatten())