# Generated by Django 4.0.5 on 2022-07-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='User', max_length=100),
        ),
    ]