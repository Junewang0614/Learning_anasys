from django.urls import path
from . import views # 在当前文件夹中导入views模块
urlpatterns = [
    path('',views.loginpage),
    # path('index/')
    path('index/',views.login)
]