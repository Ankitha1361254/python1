list3=[]
for i in range(1,11,1):
    list3.append(str(3)+"*"+str(i)+"="+str(3*i))
list4=[]
for i in range(1,11,1):
    list4.append(str(4)+"*"+str(i)+"="+str(4*i))
list5=[]
for i in range(1,11,1):
    list5.append(str(5)+"*"+str(i)+"="+str(5*i))
listM=[]
for i in range(0,10,1):
    listM.append(list3[i]+"\t"+list4[i]+"\t"+list5[i])
for i in range(0,10,1):
    print(listM[i])

    


