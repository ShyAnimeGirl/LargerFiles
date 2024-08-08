# LargerFiles
A small Python script which takes two input directories and outputs a list of the LARGER files between those two directories. 

This script requires BOTH directories to contain the exact same number of files and both folders must contain files with the exact same names, the script does no advanced checking of these requirements so it is up to you.

Most file explorers when merging files of the same name will allow you to automatically keep the larger of the two files, but there is never an option to automatically keep only the smaller of the two files, this script allows for this and is very useful when trying to compress a large amount of files that sometimes do not benefit from compression such as images. 

### Useage
I use this script to find and delete images that were not reduced in file size due to compression.

First I take my folder containing files I wish to compress and duplicate it.
Then I run my compression on the files
Now I use the script: 
```
python3 largerfiles.py /path/to/folder/1 /path/to/folder/1copy >bigger.txt
```
This will generate a text file containing the larger files between the two folders, next I run the following command:
```
xargs -d '\n' rm < bigger.txt
```
This will delete each file inside of the text file. 
Finally I simply merge the two folders together which gives me only the smaller files. 

### Common Issues:
If an error occurs it is printed in the output, so check your text file first before running the xargs command! 

Because I use this to compress images occasionally I run into the following problem; I will have a file named something like image.jpg and a file named image.png. When I compress the files to all be jpegs my compression system will overwrite or ignore one of those files, thus making my compressed directory have one less file in it than the original directory and this makes the script not work. The files causing this can sometimes be hard to locate, so my solution is to split the different file types into separate folders and run the script multiple times. 
