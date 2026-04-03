from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from usersapp.permissions import DashboardPermission
from recordsapp.models import FinancialRecord
from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth, TruncMonth

# Create your views here.

class DashboardDataView(APIView):
    permission_classes = [DashboardPermission]

    def get(self, request):
        # Total income and expenses
        total_income = FinancialRecord.objects.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        total_expenses = FinancialRecord.objects.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        net_balance = total_income - total_expenses
        category_totals = FinancialRecord.objects.values('category').annotate(total=Sum('amount')).order_by('-total')[:5]
        recent_transactions = FinancialRecord.objects.order_by('-date')[:5]
        recent_data = [
            {
                'amount': record.amount,
                'type': record.type,
                'category': record.category,
                'date': record.date,
            }
            for record in recent_transactions
        ]

        monthly_trends = FinancialRecord.objects.annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
        data = {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_balance': net_balance,
            'category_totals': category_totals,
            'recent_activity': recent_data,
            'monthly_trends': monthly_trends,
        }
        return Response(data)