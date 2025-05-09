import mod_toolbox1 as tb1
result=tb1.even1()
print(result)

result=tb1.odd1()
print(result)


result=tb1.prime1()
print(result)

def fact1():
    list1=[]
    for j in range(2,10,1):
        num1=j    
        fact1=1
        for i in range(1,num1,1):
            fact1=fact1*num1
            num1=num1-1
        list1.append(fact1)
    return list1
result=fact1()
print(result)

fact2=1
num1=5
for i in range(1,num1+1,1):
    fact2=fact2*i
print(fact2)
