from django.db import models
from django.conf import settings

# Create your models here.

class FinancialRecord(models.Model):

    Type_choices = (
        ('expense', 'Expense'),
        ('income', 'Income'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    type = models.CharField(max_length=10, choices=Type_choices)
    category = models.CharField(max_length=50)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"