# Generated by Django 5.0.6 on 2024-11-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_delete_assignedcontacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactitem',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contactitem',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]