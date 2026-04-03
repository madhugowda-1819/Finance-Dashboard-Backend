from django.contrib import admin
from .models import FinancialRecord

# Register your models here.

@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'category', 'date', 'created_at')
    list_filter = ('type', 'category', 'date')
    search_fields = ('user__username', 'category', 'type', 'amount')