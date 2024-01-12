from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Card(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateField()
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Installments(models.Model):
    installments_number = models.IntegerField()
    installment_amount = models.IntegerField()
    date = models.DateField()
    id_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.installments_number


    