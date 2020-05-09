import cv2

import math

#Train
count = 0
videoFile = "Tom and jerry.mp4"
cap= cv2.VideoCapture('C:\\Users\\Saurav Akolia\\Desktop\\u\\hackerearth\\EmotionDetection\\New Folder\\f.mp4')
# frameRate = cap.get(5) #frame rate
# x=1
# while(cap.isOpened()):
# 	frameId = cap.get(1) #current frame number

# 	ret, frame = cap.read()

# 	if (ret != True):
# 		break
# 	if (frameId % math.floor(frameRate) == 0):
# 		filename ="test%d.jpg" % count;count+=1

# 	cv2.imwrite(filename, frame)

# cap.release()
# cv2.destroyAllWindows()

frameRate = cap.get(5)
i=0
count = 0
while(cap.isOpened()):

	cap.set(cv2.CAP_PROP_POS_FRAMES, count)

	count += math.floor(frameRate)
	print(count)

	ret, frame = cap.read()
	# cv2.imshow('frame',frame)



	if (ret != True) or cv2.waitKey(1) & 0xFF == ord('q') or count>=8912:
		break

	cv2.imwrite("frames"+"\\"+"f"+str(i)+".png",frame)
	i+=1


cap.release()
cv2.destroyAllWindows()