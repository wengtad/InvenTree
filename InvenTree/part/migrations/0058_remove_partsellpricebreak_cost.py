# Generated by Django 3.0.7 on 2020-11-10 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0057_remove_partsellpricebreak_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partsellpricebreak',
            name='cost',
        ),
    ]
