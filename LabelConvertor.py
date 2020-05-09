
# def update(filename, lineno, column, text):
#     fro = open(filename, "rb")

#     current_line = 0
#     while current_line < lineno - 1:
#         fro.readline()
#         current_line += 1

#     seekpoint = fro.tell()
#     frw = open(filename, "r+b")
#     frw.seek(seekpoint, 0)

#     # read the line we want to update
#     line = fro.readline()
#     chars = line[0: column-1] + text + line[column-1:]

#     while chars:
#         frw.writelines(chars)
#         chars = fro.readline()

#     fro.close()
#     frw.truncate()
#     frw.close()


# if __name__ == "__main__":
#     update("try.txt", 1, 1, "History ")


# import os             
# # all_files = os.listdir("labels/") 


# # all_files=[]
# # import os
# # for file in os.listdir("labels"):
# #     if file.endswith(".txt"):
# #        all_files.append(file)

# # for x in all_files:
# # 	fin=open(x,'rb')

# file=open("try.txt",'rb')
# fro=open("try.txt","r+b")
# all_lines = file.readline()
# print((all_lines))

# # read_it = file.read().splitlines()
# print(file.readline())

# print('xxxxx')
# for x in file:
#   print(x)
# # print((all_lines[0][1]))


# with open('path/to/input/file') as infile, open('path/to/output/file', 'w') as outfile:
#     for line in infile:
#         for src, target in replacements.iteritems():
#             line = line.replace(src, target)
#         outfile.write(line)


# fin = open("try.txt", "rt")
# #output file to write the result to
# fout = open("out.txt", "wt")
# #for each line in the input file
# for line in fin:
# 	#read replace the string and write to output file
# 	fout.write(line.replace('1', '5'))
# 	fout.write(line.replace('0','6'))
# #close input and output files
# fin.close()
# fout.close()


import os             
# all_files = os.listdir("labels/") 


all_files=[]
import os
for file in os.listdir("labels"):
    if file.endswith(".txt"):
       all_files.append(file)


for x in all_files:

	fin = open("labels\\"+x, "rt")
# Lines=fin.readlines()
# count = 0

# for line in Lines: 
#     print(line.strip())
#     print(line.strip()[0])  
    # print("Line{}: {}".format(count, line.strip())) 

 
# #output file to write the result to
	fout = open("neoLabels\\"+x, "wt")
# #for each line in the input file
	for line in fin:
		#read replace the string and write to output file
		s=line.strip()

		if(s[0]=='1'):
			s = s[:0] +'0'+ s[0+1:]
			fout.write(s)
		else:
			s = s[:0] +'1'+ s[0+1:]
			fout.write(s)	
		fout.write('\n')				

	fin.close()
	fout.close()	

	
	
#close input and output files

