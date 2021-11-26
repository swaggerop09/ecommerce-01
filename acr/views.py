from django.shortcuts import render
from acr.models import raw
# Create your views here.

def product(request):
    a = raw.objects.all()
    return render(request,'product.html',{ 'asap' : a })
