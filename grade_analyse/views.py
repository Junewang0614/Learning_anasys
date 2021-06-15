from django.shortcuts import render

# Create your views here.
def to_gradeAnalyse(request):
    return render(request,'grade_analyse.html')