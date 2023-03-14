#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2

myimg=[r'mrimg1.jpg',r'mrimg2.jpg',r'mrimg3.jpg']
imgs = []

for i in range(len(myimg)):
    imgs.append(cv2.imread(myimg[i]))
    imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)

# Original imahe
cv2.imshow('1',imgs[0])
cv2.imshow('2',imgs[1])
cv2.imshow('3',imgs[2])

stitchy=cv2.Stitcher.create()
(dummy,Result)=stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
    print("Unsuccessful")
else:
    print('Successful')


cv2.imshow('Mount Rushmore!!',Result)

cv2.waitKey(0)


# reference::
#         https://www.geeksforgeeks.org/opencv-panorama-stitching/

# In[ ]:




