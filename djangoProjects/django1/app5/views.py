from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app5/index.html',{'param1':"hello world"})