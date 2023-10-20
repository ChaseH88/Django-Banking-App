from django.contrib import admin
from banking_app.models.transaction import Transaction
from banking_app.models.account import Account

admin.site.register(Account)
admin.site.register(Transaction)
