f1=open("marks.txt","r")
names=[]
english=[]
for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    s2=list1[3]
    list2=s2.split(":")
    english.append(list2[1])
    
maxEng=max(english)

print(names)
print(english)
print(maxEng)
