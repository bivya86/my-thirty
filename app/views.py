from django.shortcuts import render

# Create your views here.

def usd(request):
    d={'data':'hai HARshad SiR'}
    return render(request,'usd.html',d)
