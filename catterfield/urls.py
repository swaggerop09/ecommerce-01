
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('acr.urls')),
    path('login/',include('login.urls')),
]
