# Generated by Django 4.2.7 on 2023-12-03 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userform',
            name='user_id',
        ),
    ]
