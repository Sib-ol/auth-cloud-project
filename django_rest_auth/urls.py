from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ This is the key line to add
    path('api/', include('social_accounts.urls')),
]
