from django.contrib import admin
from .models import *

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to Admin Panel"

admin.site.register(Order)
admin.site.register(Product)