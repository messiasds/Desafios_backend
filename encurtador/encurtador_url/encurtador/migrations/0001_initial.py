# Generated by Django 3.1 on 2020-08-26 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=100)),
                ('new_url', models.CharField(max_length=10)),
                ('validade', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
