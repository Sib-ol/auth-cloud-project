from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
def home(request):
    return JsonResponse({
        "message": "🚀 Welcome to your Django REST API!",
        "auth_routes": "/api/v1/auth/",
        "social_routes": "/api/v1/social/"
    })

urlpatterns = [
    path('', home),  # ✅ This handles the root URL
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include("accounts.urls")),
    path('api/v1/social/', include('social_accounts.urls')),
]

