def even1():
    list1=[]
    for i in range(1,11,1):
        list1.append(2*i)
    return list1

def odd1():
    list1=[]
    for i in range(0,10,1):
        list1.append(2*i+1)
    return list1

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
