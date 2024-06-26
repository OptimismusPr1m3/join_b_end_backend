# Generated by Django 5.0.6 on 2024-06-11 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('priority', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=20)),
                ('subtasks', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('uniqueIndex', models.DecimalField(decimal_places=50, max_digits=50)),
                ('assignedContacts', models.ManyToManyField(default=None, to='tasks.assignedcontacts')),
            ],
        ),
    ]
