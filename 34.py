f1=open("marks.txt","r")
names=[]
subjects=[]
sub1=[]
toppersSub1=[]
sub2=[]
toppersSub2=[]
sub3=[]
toppersSub3=[]
sub4=[]
toppersSub4=[]
sub5=[]
toppersSub5=[]
for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    
    s2=list1[3]
    list2=s2.split(":")
    subjects.append(list2[0])
    sub1.append(int(list2[1]))
    

    s2=list1[4]
    list2=s2.split(":")
    subjects.append(list2[0])
    sub2.append(int(list2[1]))

    s2=list1[5]
    list2=s2.split(":")
    subjects.append(list2[0])
    sub3.append(int(list2[1]))

    s2=list1[6]
    list2=s2.split(":")
    subjects.append(list2[0])
    sub4.append(int(list2[1]))

    s2=list1[7]
    list2=s2.split(":")
    subjects.append(list2[0])
    sub5.append(int(list2[1]))
                
maxSub1=max(sub1)
maxSub2=max(sub2)
maxSub3=max(sub3)
maxSub4=max(sub4)
maxSub5=max(sub5)
#print(names)
#print(sub1)
#print(sub2)
#print(maxSub1)
#print(maxSub2)

for i in range(0,26,1):
    if sub1[i]==maxSub1:
        toppersSub1.append(names[i])
    if sub2[i]==maxSub2:
        toppersSub2.append(names[i])
    if sub3[i]==maxSub3:
        toppersSub3.append(names[i])
    if sub4[i]==maxSub4:
        toppersSub4.append(names[i])
    if sub5[i]==maxSub5:
        toppersSub5.append(names[i])
print(toppersSub1,"are the toppers in ",subjects[0]," with marks",maxSub1)
print(toppersSub2,"are the toppers in ",subjects[1]," with marks",maxSub2)
print(toppersSub3,"are the toppers in ",subjects[2]," with marks",maxSub3)
print(toppersSub4,"are the toppers in ",subjects[3]," with marks",maxSub4)
print(toppersSub5,"are the toppers in ",subjects[4]," with marks",maxSub5)      
