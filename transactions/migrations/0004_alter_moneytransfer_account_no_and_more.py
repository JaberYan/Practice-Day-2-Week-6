# Generated by Django 4.2.7 on 2023-12-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_moneytransfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneytransfer',
            name='account_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moneytransfer',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
