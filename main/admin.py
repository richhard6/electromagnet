from django.contrib import admin

from .models import Service, Tender, Curriculum, Stock

admin.site.register(Service)
admin.site.register(Tender)
admin.site.register(Curriculum)
admin.site.register(Stock)