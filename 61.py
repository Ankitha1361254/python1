import mod_toolbox1 as tb1
result=tb1.even1()
#print(result)

result=tb1.odd1()
#print(result)

def prime1():
    list1=[]
    for j in range(2,21,1):
        num1=j
        isPrime=True
        for i in range(2,num1,1):
            if(num1%i==0):
                isPrime=False
                break
            else:
                continue
        if(isPrime):
           list1.append(num1) 
    return list1
result=prime1()
print(result)
