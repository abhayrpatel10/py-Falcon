import os

#the path in which the files and directories to be counted
PATH=''

FilesCount=0
DirsCount=0

for root,dirs,files in os.walk(PATH):
    for directories in dirs:
        DirsCount=DirsCount+1
    for files in files:
        FilesCount=FilesCount+1

print("Number of files",FilesCount)
print("Number of directories",DirsCount)            