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

#print(perm3("PEN"))
#print(perm3("DRY"))
#print(perm3("COW"))

def perm4(s4):
    list4=[]
    part1=s4[0:1]
    part2=s4[1:4]
    temp=perm3(part2)
    len1=len(temp)
    for i in range(0,len1,1):
        list4.append(part1+temp[i])

    part1=s4[1:2]
    part2=s4[0:1]+s4[2:4]
    temp=perm3(part2)
    len1=len(temp)
    for i in range(0,len1,1):
        list4.append(part1+temp[i])

    part1=s4[2:3]
    part2=s4[0:2]+s4[3:4]
    temp=perm3(part2)
    len1=len(temp)
    for i in range(0,len1,1):
        list4.append(part1+temp[i])

    part1=s4[3:4]
    part2=s4[0:3]
    temp=perm3(part2)
    len1=len(temp)
    for i in range(0,len1,1):
        list4.append(part1+temp[i])
    return list4
#print(perm4("FAST"))
#print(perm4("ABCD"))








