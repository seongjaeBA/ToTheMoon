from django.http.response import HttpResponse
# import django.http as http
from django.shortcuts import render
from blogttm.models import Git, CaseStudy, Cloud, DataAnalysis, DjangoContents

# Create your views here.

def main(request):

    contents_list = ['Git', 'CaseStudy', 'Cloud', 'DataAnalysis']
    #일단 작성
    context = {
        'Git': 1,
        'CaseStudy': 2 ,
        'Cloud': 3,
        'DataAnalysis': 4,
        }

    for i in contents_list:
        print(i)

    return render(request, 'main.html', context=context)

def Git(request):
    return HttpResponse('ong')

def DataAnalysis(request):
    return HttpResponse('ong')

def Cloud(request):
    return HttpResponse('ong')

def CaseStudy(request):
    return HttpResponse('ong')

def DjangoContents(request):
    return HttpResponse('ong')