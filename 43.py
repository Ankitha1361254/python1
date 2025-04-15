def perm3(s3):
    
    
    c1=s3[0:1]
    c2=s3[1:2]
    c3=s3[2:3]
    
    list3=[]
    list3.append(c1+c2+c3)#PEN Added
    list3.append(c1+c3+c2)#PNE added
    list3.append(c2+c1+c3)#EPN added
    list3.append(c2+c3+c1)#ENP added
    list3.append(c3+c1+c2)#NPE added
    list3.append(c3+c2+c1)#NEP added
    
    return list3

print(perm3("PEN"))
print(perm3("DRY"))
print(perm3("COW"))

def perm4(s4):
    list4=[]

    for i in range(4):
        c1=s4[i:i+1]
        c2=s4[:i]+s4[i+1:]
        for j in perm3(c2):
            list4.append(c1+j)

    return list4
print(perm4("Fast"))
print(perm4("GIRL"))


def perm5(s5):
    list5=[]

    for i in range(5):
        c1=s5[i:i+1]
        c2=s5[:i]+s5[i+1:]
        for j in perm4(c2):
            list5.append(c1+j)

    return list5
print(perm5("SMILE"))
print(perm5("CLOTH"))







