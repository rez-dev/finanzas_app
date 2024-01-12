from django.contrib import admin
from .models import Category, User, Card, Transaction, Installments
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Installments)