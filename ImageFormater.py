from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
import pandas as pd 
import cv2
import os

def stringreplace(dir,cur_file,new_file):
	os.chdir(dir)

	# for replacing the path of train location
	fin = open(cur_file, "rt")
	fout=open(new_file,"wt")
		for line in fin:
		fout.write(line.replace('data/obj/img/','C:\\Users\\Saurav Akolia\\Google Drive\\darknet\\sad\\'))
		# fout.write(line.replace('.png','.jpg'))
	fin.close()
	fout.close()

def format_convertor(dir):
	WINDOWS_LINE_ENDING = b'\r\n'
	UNIX_LINE_ENDING = b'\n'

		# relative or absolute file path, e.g.:
	file_path = r"sart.txt"

	with open(file_path, 'rb') as open_file:
		content = open_file.read()

	content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

	with open(file_path, 'wb') as open_file:
		open_file.write(content)


def text_formater(dir,textfile):
	os.chdir(dir)

	file1 = open(textfile, 'r') 

	i=0
	my_file=[]
	Lines = file1.readlines() 
	for line in Lines: 
	    s=line.strip()
	    if(len(s)>=18 and s[18]=='C'):
	    	i=i+1
	    my_file.append(s)
	 
	 d={'Location':str,
	'Tom':int,
	'Jerry':int,
	'TL':int,
	'TT':int,
	'TW':int,
	'TH':int,
	'JL':int,
	'JT':int,
	'JW':int,
	'JH':int}
	df = pd.DataFrame(index=range(i),columns=['Location','Tom','Jerry','TL','TT','TW','TH','JL','JT','JW','JH'])
	for col in df.columns:
	    df[col].values[:] = 0

	df=df.astype(d)    
	df = pd.DataFrame(['Location','Tom','Jerry','TL','TT','TW','TH','JL','JT','JW','JH']) 

	k=-1
	c=0
	for x in my_file:
		x=x.split()

		if(k<=i-2 and x[0]=='Enter'):
			k=k+1
			df.loc[df.index[k],'Location']=x[3]+' '+x[4][0:-1]			

		if(x[0]=='Tom:'):
			print(k)
			df.loc[df.index[k],'Tom']=1
			df.loc[df.index[k],'TL']=int(x[3])
			df.loc[df.index[k],'TT']=int(x[5])
			df.loc[df.index[k],'TW']=int(x[7])
			df.loc[df.index[k],'TH']=int((x[9])[0:-1])
			
		if(x[0]=='Jerry:'):
			df.loc[df.index[k],'Jerry']=1
			df.loc[df.index[k],'JL']=int(x[3])
			df.loc[df.index[k],'JT']=int(x[5])
			df.loc[df.index[k],'JW']=int(x[7])
			df.loc[df.index[k],'JH']=int((x[9])[0:-1])
					
	df.loc[df.index[k],'Location']=my_file[-3].split()[3]+' '+my_file[-3].split()[4]

	df.to_csv('sadresult.csv')
	return df

def image_cropper(df,save_dir):
	df=pd.read_csv('testresult.csv')
	c=0
	for x in df.index:
		print(df['Location'][x])
		im = cv2.imread(df['Location'][x])

		if(df['Tom'][x]):
			x1, y1, width, height =df['TL'][x],df['TT'][x],df['TW'][x],df['TH'][x]
			x2, y2 = x1 + width, y1 + height
			crop_img = im[y1:y2, x1:x2]
			cv2.imwrite(save_dir+df['Location'][x][75:], crop_img)
			cv2.waitKey(0)
			c=c+1

		elif(df['Jerry'][x]):
			x1, y1, width, height =df['JL'][x],df['JT'][x],df['JW'][x],df['JH'][x]
			x2, y2 = x1 + width, y1 + height
			crop_img = im[y1:y2, x1:x2]
			# cv2.imshow("cropped", crop_img)
			cv2.imwrite(save_dir+df['Location'][x][75:],crop_img)
			cv2.waitKey(0)
			c=c+1

		
		else:
			cv2.imwrite(save_dir+df['Location'][x][75:],im)
			cv2.waitKey(0)
			c=c+1	