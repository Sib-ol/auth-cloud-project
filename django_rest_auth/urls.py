from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 👇 Add this line for your auth APIs
    path('api/', include('auth_app.urls')),  # Replace 'auth_app' with your app name
]
