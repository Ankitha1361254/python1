from django.shortcuts import render

# Create your views here.
def home(request):
    n1=6
    result1=squares()
    result2=fact(n1)
    return render(request,"app3/index.html",{"param1":result1,"param2":result2,"param3":n1})
def squares():
    result=[]
    for i in range(1,11,1):
        result.append(i*i)
    return result
def fact(n1):
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1