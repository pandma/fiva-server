# Generated by Django 4.0.5 on 2022-07-12 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constact_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=255)),
                ('state', models.CharField(default='Pocessing', max_length=100)),
            ],
        ),
    ]
