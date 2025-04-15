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

s4="FAST"
c1=s4[0:1]
c2=s4[1:4]
list4=[]
c3=perm3(c2)
for i in c3:
    list4.append(c1+i)
print(list4)




