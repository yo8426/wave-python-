import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

im1=cv2.imread('lena.png',0)
height=5
weight=10

[m,n]=im1.shape
im2=np.zeros([m,n])
im3=np.zeros([m,n])
im4=np.zeros([m,n])

for i in range(m):
    for j in range(n):
        # get wave
        x=int((math.sin(weight*i*3.14*2/360))*height)
        # avoid exceed matrix
        if 0<x+j<n:
            im2[i,j]=im1[i,j+x]

for i in range(m):
    for j in range(n):
        x=int((math.sin(weight*j*3.14*2/360))*height)
        if 0<x+i<m:
            im3[i,j]=im1[i+x,j]

for i in range(m):
    for j in range(n):
        x=int((math.sin(weight*j*3.14*2/360))*height)
        y=int((math.sin(weight*i*3.14*2/360))*height)
        if 0<x+i<m and 0<y+j<n:
            im4[i,j]=im1[i+x,j+y]
        
plt.figure()
plt.suptitle('compare : height='+str(height)+', weight='+str(weight))
plt.subplot(2,2,1)
plt.title('original')
plt.imshow(im1)
plt.subplot(2,2,2)
plt.title('horizontal')
plt.imshow(im2)
plt.subplot(2,2,3)
plt.title('vertical')
plt.imshow(im3)
plt.subplot(2,2,4)
plt.title('horizontal + vertical')
plt.imshow(im4)
plt.show()