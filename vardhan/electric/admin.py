from django.contrib import admin
from .models import Product
# Register your models here.
class prodAdmin(admin.ModelAdmin):
    list_display = ['proname','proprice']


admin.site.register(Product)
