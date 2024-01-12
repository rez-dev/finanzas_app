from rest_framework import serializers
from .models import Category, User, Card, Transaction, Installments

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class InstallmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installments
        fields = '__all__'

        