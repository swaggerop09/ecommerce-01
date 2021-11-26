from django.contrib import admin
from .models import categories, raw
# Register your models here.

admin.site.register(raw)
admin.site.register(categories)