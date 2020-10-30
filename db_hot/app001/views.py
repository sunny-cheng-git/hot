from django.shortcuts import render,HttpResponse


def index(request):


    return HttpResponse('<h1>首页</h1>')
