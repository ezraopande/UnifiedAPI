from django.contrib import admin

from api.models import Product, Sliders, Configs

# Register your models here.

admin.site.register(Product)
admin.site.register(Sliders)
admin.site.register(Configs)
