# Generated by Django 4.2.6 on 2023-10-20 14:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveIntegerField(default=68142245, unique=True, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('account_pin', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('account_type', models.CharField(choices=[('checking', 'Checking'), ('savings', 'Savings')], default='checking', max_length=8)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')], default='deposit', max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='banking_app.account', to_field='account_number')),
            ],
        ),
    ]
