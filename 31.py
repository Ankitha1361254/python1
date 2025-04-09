f1=open("marks.txt","r")
names=[]
english=[]
toppersEng=[]
maths=[]
toppersMat=[]
for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    
    s2=list1[3]
    list2=s2.split(":")
    english.append(int(list2[1]))

    s2=list1[4]
    list2=s2.split(":")
    maths.append(int(list2[1]))
maxEng=max(english)
maxMat=max(maths)
#print(names)
#print(english)
#print(maths)
#print(maxEng)
#print(maxMat)
for i in range(0,26,1):
    if english[i]==maxEng:
        toppersEng.append(names[i])
    if maths[i]==maxMat:
        toppersMat.append(names[i])
print(toppersEng, "are the toppers in English with marks",maxEng)
print(toppersMat,"are the toppers in Maths with marks",maxMat)
       
