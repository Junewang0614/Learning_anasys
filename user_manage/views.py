from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def loginpage(request):
    return render(request,'user_manage/login.html')

def login(request):
    uname = request.POST.get('uname',"") # 如果没找到，则赋空值
    pword = request.POST.get('pword',"")

    if uname and pword:
        # return HttpResponse("hello!"+uname)
        return render(request,'user_manage/index.html')
    else:
        return HttpResponse("sorry!")

