#!/usr/bin/python

# list the name of the current working directory

import os
print(os.getcwd())




# files in the current working directory


my_files = os.listdir()
print(my_files)
 



# List the size of files in the current working directory

my_files = [ (file_path, os.stat(file_path).st_size) 
                    for file_path in my_files ]
print(my_files)                    
                    

# store files in a dictionary

import os

path = '.'

files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)
    file_size = os.path.getsize(file_path)
    print("Path: {}, File: {}, Size: {} bytes".format(file_path, file, file_size))