from django.shortcuts import render

# Create your views here.
def home(request):
    output=date1
    return render(request,'app2/index.html',{'param1':output})
def date1():
    import datetime as dt
    today=dt.datetime.now()
    y1=str(today.year)
    M1=str(today.month)
    d1=str(today.day)
    return d1+" "+M1+" "+y1