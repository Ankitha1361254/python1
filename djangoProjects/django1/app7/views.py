from django.shortcuts import render

# Create your views here.
def home(request):
    n1=3
    n2=8
    result=factn(n1,n2)
    facts=result[0]
    nums=result[1]

    return render(request,'app7/index.html',{'param1':nums,'param2':facts})
def fact(n):
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return fact1
def factn(n1,n2):
    list1=[]
    list2=[]
    for i in range(n1,n2+1,1):
        list1.append(fact(i))
        list2.append(i)
    return list1,list2
