from django.shortcuts import render


def index(request):
    return  render(request,'newapp/index.html')
def about(request):
    return render(request,'newapp/about.html')