from django.shortcuts import render
from rest_framework import viewsets
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from usersapp.permissions import RecordPermission
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class FinancialRecordViewSet(viewsets.ModelViewSet):
    
    serializer_class = FinancialRecordSerializer
    permission_classes = [RecordPermission]  # Allow unrestricted access for testing purposes, adjust as needed

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return FinancialRecord.objects.filter(is_deleted=False)
        return FinancialRecord.objects.none()
    
    def perform_destroy(self, instance):
        isinstance.is_deleted = True
        instance.save()

    # Assign logged-in user automatically
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)