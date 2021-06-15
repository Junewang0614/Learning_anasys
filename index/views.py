from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

#跳转到登录页面的函数
def toLogin(request):
    return render(request,'login.html')

#登录逻辑
def main(request):
    print(request)
    name=request.GET.get('username','')
    pwd=request.GET.get('password','')
    if name and pwd:
        print(StudentInfo.objects.all())
        c=StudentInfo.objects.filter(stu_id=name,stu_psw=pwd).count()

        if c==1:
            request.session['username'] = name
            return render(request,'index.html')
        else:
            return HttpResponse('登录失败')

#跳转到成绩分析页面的函数
def togradeAnalyse(request):

    return redirect('/grade_analyse/')

#跳转到对话流分析页面的函数
def tochatflowAnalyse(request):

    return redirect('/chatflow_analyse/')

