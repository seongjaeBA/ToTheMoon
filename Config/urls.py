"""ToTheMoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# from blogttm import views

#url(정규표현식, 뷰)
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('',views.main, name='ToTheMoon'),
# ]

# urlpatterns += [
#     path('ToTheMoon/', include('blogttm.urls')),
# ]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

# urlpatterns += [
#     path('', RedirectView.as_view(url='/ToTheMoon/', permanent=True)),
# ]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #블로그 ToTheMoon 안의 앱만 실행되도록 
    path('ToTheMoon/', include('blogttm.urls')),
    path('', RedirectView.as_view(url='/ToTheMoon/', permanent=True)),
    
    path("dashboard/", include("authentication.urls")), # Auth routes - login / register
    path("dashboard/", include("dashboard.urls"))             # UI Kits Html files
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)