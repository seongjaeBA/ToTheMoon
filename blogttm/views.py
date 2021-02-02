from django.http.response import HttpResponse
# import django.http as http
from django.shortcuts import render
from blogttm.models import GitModels, CaseStudyModels, CloudModels, DataAnalysisModels, DjangoContentsModels

# Create your views here.


def main(request):
    #일단 작성
    context = {
        "name":"main",
        }
    return render(request, 'main.html', context=context)



def Git(request):
    latest_post = GitModels.objects.all
    context = {
        "name": "Git",
        "posts": latest_post,
        "photo": "../../static/images/yancy-min-842ofHC6MaI-unsplash.jpg",
    }
    return render(request, 'main.html', context=context)

def DataAnalysis(request):
    latest_post = DataAnalysisModels.objects.all
    context = {
        "name": "Data Analysis",
        "posts": latest_post,
        "photo": "../../static/images/luke-chesser-JKUTrJ4vK00-unsplash.jpg",
    }
    return render(request, 'main.html', context=context)

def Cloud(request):
    latest_post = CloudModels.objects.all
    context = {
        "name": "Cloud",
        "posts": latest_post,
        "photo": "../../static/images/c-dustin-K-Iog-Bqf8E-unsplash.jpg",
    }
    return render(request, 'main.html', context=context)

def CaseStudy(request):
    latest_post = CaseStudyModels.objects.all
    context = {
        "name": "Case Study",
        "posts": latest_post,
        "photo": "../../static/images/kelly-sikkema-v9FQR4tbIq8-unsplash.jpg",
    }
    return render(request, 'main.html', context=context)

def DjangoContents(request):
    latest_post = DjangoContentsModels.objects.all
    
    context = {
        "name": "Django",
        "posts" : latest_post,
        "photo": "../../static/images/django.png",
    }
    return render(request, 'main.html', context=context)

def posting(request, pk):
    post = DjangoContentsModels.objects.get(pk=pk)
    context = {
        "name": "detailpage",
        "post" : post,
    }
    return render(request, 'main.html', context=context)

# def post_add(request):
#     return render(request, 'blog/post_add.html')