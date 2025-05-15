import os
dir1="C:\Test1"
#print(dir1)
list1=list(os.walk(dir1))
c1=list1[0]
#print(c1)
path=c1[0]
dirs=c1[1]
files=c1[2]
print(path)
print(dirs)
print(files)
