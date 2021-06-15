from django.shortcuts import render

# Create your views here.
def to_chatflowAnalyse(request):
    return render(request,'chatflow_analyse.html')