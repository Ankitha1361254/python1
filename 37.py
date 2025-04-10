def goldMedal(fname):
    
    f1=open(fname,"r")
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
    total=[]
    totalTopper=[]
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

        total.append(sub1[i]+sub2[i]+sub3[i]+sub4[i]+sub5[i])

                   
    maxSub1=max(sub1)
    maxSub2=max(sub2)
    maxSub3=max(sub3)
    maxSub4=max(sub4)
    maxSub5=max(sub5)
    maxTotal=max(total)
    

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
        if total[i]==maxTotal:
            totalTopper.append(names[i])
            
    return(toppersSub1,toppersSub2,toppersSub3,toppersSub4,toppersSub5,totalTopper,subjects,maxSub1,maxSub2,maxSub3,maxSub4,maxSub5,maxTotal)

fname1="marks_school"
fname3=".txt"
for i in range(1,6,1):
    
    result1=goldMedal(fname1+str(i)+fname3)
    print(result1[0],"are the toppers in",result1[6][0],"with marks",result1[7],"from school",i)



