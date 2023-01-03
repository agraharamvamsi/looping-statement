from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'vamsi','L':[10,20,30,40,50]}
    return render(request,'looping.html',d)