"""
URL configuration for clinical_case_simulator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include 
from django.http import JsonResponse   # 👈 THÊM

def health(request):                  # 👈 THÊM
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('health/', health),  
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('predict_disease/', include('predict_disease.urls', namespace='predict_disease')),
    path('predictproc/', include('predictproc.urls', namespace='predictproc')),
]
