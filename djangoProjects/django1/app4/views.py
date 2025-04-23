from django.shortcuts import render

# Create your views here.
def home(request):
    result1=table1(3,4)
    return render(request,'app4/index.html',{'param1':result1})
def table1(n1,n2):
    list3=[]
    for j in range(n1,n2+1,1):
        for i in range(1,11,1):
            list3.append(str(j)+"*"+str(i)+"="+str(j*i))
        if j != n2:  
            list3.append("BREAK")  
    return list3

