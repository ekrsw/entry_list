from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('entryapp.urls')),
    path('', include('accounts.urls')),
]
