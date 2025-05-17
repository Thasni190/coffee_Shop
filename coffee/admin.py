from django.contrib import admin
from .models import Coffee
# Register your models here.

class CoffeeAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')

admin.site.register(Coffee, CoffeeAdmin)