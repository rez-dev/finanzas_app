# Generated by Django 5.0.1 on 2024-01-07 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('id_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.card')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.category')),
            ],
        ),
        migrations.CreateModel(
            name='Installments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installments_number', models.IntegerField()),
                ('installment_amount', models.IntegerField()),
                ('date', models.DateField()),
                ('id_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
    ]
