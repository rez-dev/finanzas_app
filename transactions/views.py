from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TransactionSerializer, CategorySerializer, UserSerializer, CardSerializer, InstallmentsSerializer
from .models import Transaction, Category, User, Card, Installments

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class InstallmentsViewSet(viewsets.ModelViewSet):
    serializer_class = InstallmentsSerializer
    queryset = Installments.objects.all()
