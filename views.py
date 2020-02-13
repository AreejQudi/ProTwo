from django.shortcuts import render
from django.http import HttpResponse
from .models import Emp


# Create your views here.
def MyPage(request):
    context = {'name': "Hi From Server"}
    return render(request, 'AppTwo/MyPage.html', context=context)


def index3(request):
    emps = Emp.objects.all()
    context = {'name': "Hi From Server" ,
               'emps': emps}
    return render(request,'AppTwo/index3.html',context=context)


def home(request):
    context = {}
    return render(request, 'AppTwo/Home.html', context=context)
