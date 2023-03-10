# Generated by Django 2.2.16 on 2022-11-10 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221110_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', help_text='Роль пользователя', max_length=9, verbose_name='Роль'),
        ),
    ]
