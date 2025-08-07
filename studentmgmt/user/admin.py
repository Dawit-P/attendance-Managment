from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_security', 'is_staff', 'is_active')
    list_filter = ('is_security', 'is_staff', 'is_active')
    search_fields = ('email',)
