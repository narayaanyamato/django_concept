# Generated by Django 4.1 on 2024-08-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conceptapp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='address',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cname',
        ),
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phone',
        ),
    ]
