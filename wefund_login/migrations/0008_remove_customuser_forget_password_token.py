# Generated by Django 4.2 on 2023-12-20 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wefund_login', '0007_alter_customuser_forget_password_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='forget_password_token',
        ),
    ]
