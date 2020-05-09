import os 
os.chdir('C:\\Users\\Saurav Akolia\\Google Drive\\darknet\\sad\\')
print(os.getcwd())



# for replacing the path of train location
fin = open("risk.txt", "rt")
fout=open("sadresult.txt","wt")
# data = fin.read()
for line in fin:
	fout.write(line.replace('data/obj/img/','C:\\Users\\Saurav Akolia\\Google Drive\\darknet\\sad\\'))
	# fout.write(line.replace('.png','.jpg'))
# data = data.replace('C:\\Users\\Saurav Akolia\\Desktop\\u\\hackerearth\\EmotionDetection\\Yolo\\Images', 'python')
fin.close()
fout.close()


# fin = open("data.txt", "wt")
# fin.write(data)
# fin.close()

#for listing directory images into folder
# dir /b /s /a:-D *.jpg > results.txt

# fin = open("test.txt", "rt")
# fout = open("te.txt", "wt")

# for line in fin:
# 	fout.write(line.replace('.jpg','.png'))
	
# fin.close()
# fout.close()


#for changing jpg to png
# Dir *.jpg | rename-item -newname { [io.path]::ChangeExtension($_.name, "png") }

# from PIL import Image
# import os

# directory = r'img'
# c=1
# for filename in os.listdir(directory):
#     if filename.endswith(".jpg"):
#         im = Image.open(directory+'\\'+filename)
#         name='img'+str(c)+'.png'
#         rgb_im = im.convert('RGB')
#         rgb_im.save(name)
#         c+=1
#         print(os.path.join(directory, filename))
#         continue
#     else:
#         continue


# import os
# image_path ='some_path/'
# for img in os.listdir(image_path):
#     input_image = Image.open(image_path+img).convert('RGB')
#     input_image.save(image_path+img + ".png", "PNG")        

