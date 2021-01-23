from blogttm.admin import Git
from django.urls import path, include
from blogttm import views


urlpatterns = [
    path('', views.main, name='main'),
    path('git/', views.Git, name= 'Git'),
    path('DataAnalysis/', views.DataAnalysis, name='DataAnalysis'),
    path('CaseStudy/', views.CaseStudy, name='CaseStudy'),
    path('Cloud/', views.Cloud, name='Cloud'),
    path('DjangoContents/', views.DjangoContents, name='DjangoContents'),
]