from django.contrib import admin
from .models import Domain, Alias

# Register your models here.
admin.site.register(Domain)
admin.site.register(Alias)
