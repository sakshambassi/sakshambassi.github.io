import cv2
import glob
f = "/home/saksham/Resume/sakshambassi.github.io/images/onion-before.png"
im = cv2.imread(f)
# size = im.shape[0]
# if(size>im.shape[1]):
# 	size=im.shape[1]
size = 150
im = im[0:size, 0:size]
cv2.imwrite(f,im)