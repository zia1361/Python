from django.contrib import admin

from .models import Order, Pizza, User

# Register your models here. 
admin.site.register(Order)
admin.site.register(Pizza)
admin.site.register(User)
