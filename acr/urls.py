from django.urls import path
from acr.views import product

urlpatterns = [
    path('v/',product),
]