from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import host, visit, visitor

# Register your models here.
class hostInline(admin.StackedInline):
    model = host
    can_delete = False
    verbose_name_plural = 'host'

class UserAdmin(BaseUserAdmin):
    inlines = (hostInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(visit)
admin.site.register(visitor)
admin.site.register(host)

