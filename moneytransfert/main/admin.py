from django.contrib import admin

# Register your models here.
from .models import Transaction, TransactionHistory

admin.site.register(Transaction)
admin.site.register(TransactionHistory)
