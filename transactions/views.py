from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import Response
from .serializer import TransactionSerializer, CategorySerializer, UserSerializer, CardSerializer, InstallmentsSerializer
from .models import Transaction, Category, User, Card, Installments
from rest_framework.decorators import action

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    @action(detail=False, methods=['get'])
    def get_transactions_by_user(self, request, pk=None):
        id_user = self.request.query_params.get('id_user', None)
        if id_user:
            queryset = Transaction.objects.filter(id_user=id_user)
        else:
            queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_transactions_by_user_and_category(self, request, pk=None):
        id_user = self.request.query_params.get('id_user', None)
        id_category = self.request.query_params.get('id_category', None)
        if id_user and id_category:
            queryset = Transaction.objects.filter(id_user=id_user, id_category=id_category)
        else:
            queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def get_transactions_by_name(self, pk=None):
        name = self.request.query_params.get('name', None)
        if name:
            user = User.objects.filter(name=name)
            queryset = Transaction.objects.filter(id_user=user[0].id)
        else:
            queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def calculate_income_by_card(self, pk=None):
        id_user = self.request.query_params.get('id_user', None)
        id_card = self.request.query_params.get('id_card', None)
        if id_user and id_card:
            queryset = Transaction.objects.filter(id_user=id_user, id_card=id_card, type='Ingreso')
            total = 0
            for transaction in queryset:
                total += transaction.amount
        else:
            total = 0
        return Response({'total': total})
    
    @action(detail=False, methods=['get'])
    def calculate_expense_by_card(self, pk=None):
        id_user = self.request.query_params.get('id_user', None)
        id_card = self.request.query_params.get('id_card', None)
        if id_user and id_card:
            queryset = Transaction.objects.filter(id_user=id_user, id_card=id_card, type='Egreso')
            total = 0
            for transaction in queryset:
                total += transaction.amount
        else:
            total = 0
        return Response({'total': total})
            

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get'])
    def get_user_by_name(self, pk=None):
        name = self.request.query_params.get('name', None)
        if name:
            queryset = User.objects.filter(name=name)
        else:
            queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class InstallmentsViewSet(viewsets.ModelViewSet):
    serializer_class = InstallmentsSerializer
    queryset = Installments.objects.all()

# obtener datos usuario por name
# class getUserByName(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     def get_queryset(self):
#         name = self.kwargs['name']
#         return User.objects.filter(name=name)
# class getUserByName(viewsets.ModelViewSet):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         name = self.request.query_params.get('name', None)
#         if name:
#             return User.objects.filter(name=name)
#         else:
#             return User.objects.all()

# obtener datos transacciones por usuario
# class getTransactionsByUser(viewsets.ModelViewSet):
#     serializer_class = TransactionSerializer
    
#     def get_queryset(self):
#         id_user = self.request.query_params.get('id_user', None)
#         if id_user:
#             return Transaction.objects.filter(id_user=id_user)
#         else:
#             return Transaction.objects.all()
        
# obtener datos transacciones por usuario y categoria
# class getTransactionsByUserAndCategory(viewsets.ModelViewSet):
#     serializer_class = TransactionSerializer
    
#     def get_queryset(self):
#         id_user = self.request.query_params.get('id_user', None)
#         id_category = self.request.query_params.get('id_category', None)
#         if id_user and id_category:
#             return Transaction.objects.filter(id_user=id_user, id_category=id_category)
#         else:
#             return Transaction.objects.all()