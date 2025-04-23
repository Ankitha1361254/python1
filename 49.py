def table1(n1,n2):
    output=""
    for j in range(n1,n2+1,1):
        for i in range(1,11,1):
            output=output+str(j)+str(i)+str(j*i)+"\n"
        output=output+"\n"
    return output
print(table1(3,20))


