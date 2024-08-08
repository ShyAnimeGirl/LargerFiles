import os
import sys

#this program expects 2 dirs containing the same files and returns a list of the LARGER files!
file_list1 = []
file_list1_names = []

file_list2 = []
file_list2_names = []

if len(sys.argv) != 3:
	print("Please provide two directories as command line arguments.")
	quit()
	
dir1 = sys.argv[1]
dir2 = sys.argv[2]

for file in os.listdir(dir1):
	filename = os.path.join(dir1, file)
	filesize = os.path.getsize(filename)
	file_list1.append(filesize)
	file_list1_names.append(filename)

for file in os.listdir(dir2):
	filename = os.path.join(dir2, file)
	filesize = os.path.getsize(filename)
	file_list2.append(filesize)
	file_list2_names.append(filename)

if (len(file_list1) != len(file_list2)):
		print("both directories must contain the same number of files")
		quit()
	
	
for x in range(len(file_list1)):
	if file_list1[x] >= file_list2[x]:
		print(file_list1_names[x])
	else:
		print(file_list2_names[x])
		