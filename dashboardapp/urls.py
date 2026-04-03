from django.urls import path, include
from .views import DashboardDataView

urlpatterns = [
    path('dashboard/', DashboardDataView.as_view(), name='dashboarddata'),
]