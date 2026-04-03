from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'password', 'date_joined')
    list_filter = ('role', 'date_joined')
    search_fields = ('username', 'email')