from django.contrib import admin

from root.users.models import Permission, Role

# Register your models here.
admin.site.register(Role)
admin.site.register(Permission)
