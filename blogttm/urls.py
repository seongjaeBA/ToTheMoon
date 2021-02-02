from blogttm.admin import Git
from django.urls import path, include
from blogttm import views


urlpatterns = [
    path('', views.main, name='main'),
    path('git/', views.Git, name= 'Git'),
    path('git/<int:pk>/', views.posting, name= 'Gitdetail'),
    path('DataAnalysis/', views.DataAnalysis, name='DataAnalysis'),
    path('DataAnalysis/<int:pk>/', views.posting, name='DataAnalysisGitdetail'),
    path('CaseStudy/', views.CaseStudy, name='CaseStudy'),
    path('CaseStudy/<int:pk>/', views.posting, name='CaseStudyGitdetail'),
    path('Cloud/', views.Cloud, name='Cloud'),
    path('Cloud/<int:pk>/', views.posting, name='CloudGitdetail'),
    path('DjangoContents/', views.DjangoContents, name='DjangoContents'),
    path('DjangoContents/<int:pk>/', views.posting, name='DjangoContentsGitdetail'),
]