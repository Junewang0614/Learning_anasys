from django.urls import path, include
from django.conf.urls import  url

import grade_analyse
from . import views
from grade_analyse import views as views2
urlpatterns=[
    path('',views.toLogin),
    path('main/', views.main),
    path('temp1/',views.togradeAnalyse,name='grade_analyse'),
    path('temp2/', views.tochatflowAnalyse,name='chatflow_analyse')
    #url('grade_analyse/',views2.to_gradeAnalyse,name='grade_analyse')
    #path('',views.toAnalyse)
]