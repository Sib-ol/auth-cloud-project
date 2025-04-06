# django_rest_auth/urls.py or your main config/urls.py
from django.http import JsonResponse
from django.urls import path
from django.contrib import admin

def index(request):
    return JsonResponse({"status": "Live!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]

