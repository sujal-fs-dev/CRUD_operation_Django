# Generated by Django 5.0.4 on 2024-07-14 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_employee_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='student',
        ),
    ]
