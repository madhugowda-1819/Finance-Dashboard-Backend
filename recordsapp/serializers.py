from rest_framework import serializers
from .models import FinancialRecord
from datetime import date

class FinancialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = '__all__'
        # exclude = ['is_deleted']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def validate(self, data):
        if data["type"] not in ["income", "expense"]:
            raise serializers.ValidationError("Invalid record type.")
        return data
    
    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date cannot be in the future.")
        return value
    
    def validate_category(self, value):
       if len(value) < 3:
           raise serializers.ValidationError("Category must be at least 3 characters.")
       return value