from django.shortcuts import render,HttpResponse


def index(request):


    return HttpResponse('<h1>首页</h1>')


def Arimcan(request):

    return HttpResponse("欧美上线")

