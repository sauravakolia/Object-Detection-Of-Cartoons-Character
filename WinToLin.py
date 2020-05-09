import os             
# all_files = os.listdir("labels/") 


# all_files=[]
# import os
# for file in os.listdir("img"):
#     if file.endswith(".txt"):
#        all_files.append(file)

	# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

	# relative or absolute file path, e.g.:
file_path = r"sart.txt"

with open(file_path, 'rb') as open_file:
	content = open_file.read()

content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

with open(file_path, 'wb') as open_file:
	open_file.write(content)