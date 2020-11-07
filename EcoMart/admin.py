from django.contrib import admin
from EcoMart.models import Setting

# Register your models here.
admin.site.site_header = "Eshop"
admin.site.index_title = "Eshop's Administration"
admin.site.register(Setting)
