import mod_toolbox1 as tb1
result=tb1.even1()
print(result)

def odd1():
    list1=[]
    for i in range(0,10,1):
        list1.append(2*i+1)
    return list1
result=odd1()
print(result)

