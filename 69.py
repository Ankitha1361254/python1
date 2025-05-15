import os
dir1="C:\Test1"
list1=list(os.walk(dir1))
c1=list1[0]

c2=list1[1]
c3=list1[2]
c4=list1[3]

path=c1[0]
dirs=c1[1]
files=c1[2]

fruits1=c2[2]
fruits2=c3[2]
fruits3=c4[2]
#print(path)
#print(dirs)
#print(files)
print(fruits1)
print(fruits2)
print(fruits3)


