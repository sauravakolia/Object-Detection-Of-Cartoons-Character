# import cv2
# img = cv2.imread("train/frame0.jpg")
# crop_img = img[0:498, 0:173]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)

# (left_x:  324   top_y:  101   width:  321   height:  229)
# # (left_x:  498   top_y:  173   width:  244   height:  198)
import os
from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
import pandas as pd 
import cv2

os.chdir('C:\\Users\\Saurav Akolia\\Google Drive\\darknet\\sad\\')

print(len('C:/Users/Saurav Akolia/Google Drive/darknet/sad/'))
# print(len("C:/Users/Saurav Akolia/Desktop/u/hackerearth/EmotionDetection/Dataset/Test/"))





df=pd.read_csv('sadresult.csv')
c=0
for x in df.index:
	im = cv2.imread(df['Location'][x])
	
	if(df['Tom'][x]):
		# cod=df.to_dict[x]
		# li=[if(value<0): 0 else: value for key, value in cod.items()]
		for key in df.columns:
			if(key!='Location' and df[key][x]<0):
				df.loc[df.index[x],key]=0	
		x1, y1, width, height =df['TL'][x],df['TT'][x],df['TW'][x],df['TH'][x]
		x2, y2 = x1 + width, y1 + height
		crop_img = im[y1:y2, x1:x2]
		cv2.imwrite("sadCroped\\"+df['Location'][x][48:], crop_img)
		cv2.waitKey(0)
		c=c+1
		

	elif(df['Jerry'][x]):

		for key in df.columns:
			if(key!='Location' and df[key][x]<0):
				df.loc[df.index[x],key]=0	

		x1, y1, width, height =df['JL'][x],df['JT'][x],df['JW'][x],df['JH'][x]
		x2, y2 = x1 + width, y1 + height
		crop_img = im[y1:y2, x1:x2]
		cv2.imwrite("sadCroped\\"+df['Location'][x][48:],crop_img)
		cv2.waitKey(0)
		c=c+1
	else:
		cv2.imwrite("sadCroped\\"+df['Location'][x][48:],im)
		
		cv2.waitKey(0)
		c=c+1
	
