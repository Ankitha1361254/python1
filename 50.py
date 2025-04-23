def table1(n1,n2):
    list3=[]
    for j in range(n1,n2+1,1):
        for i in range(1,11,1):
            list3.append(str(j)+"*"+str(i)+"="+str(j*i))
    return list3
result=table1(3,4)
for i in range(0,10,1):
    print(result[i])


