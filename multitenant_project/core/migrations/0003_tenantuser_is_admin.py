# Generated by Django 4.2.11 on 2025-05-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tenantuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
