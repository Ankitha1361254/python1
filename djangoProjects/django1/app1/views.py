from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app1/index.html',{'param1':"Ankitha ",'param2':"Bhagyashree"})