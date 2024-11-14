# djangoProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('blog.urls')),  # Ensure 'blog.urls'
]
