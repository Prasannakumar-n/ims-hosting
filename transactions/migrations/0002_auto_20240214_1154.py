# Generated by Django 3.0.7 on 2024-02-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='gstin',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]