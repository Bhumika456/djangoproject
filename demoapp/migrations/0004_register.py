# Generated by Django 4.0 on 2022-01-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
