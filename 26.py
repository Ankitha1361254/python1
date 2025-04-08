f1=open("marks.txt","r")
names=[]
english=[]
for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    english.append(list1[3])



print(names)
print(english)
