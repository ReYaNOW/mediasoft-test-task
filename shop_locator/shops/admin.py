from django.contrib import admin

from shop_locator.shops.models import City, Street, Shop

admin.site.register(City)
admin.site.register(Street)
admin.site.register(Shop)
