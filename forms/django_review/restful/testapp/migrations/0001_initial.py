# Generated by Django 3.2.4 on 2021-06-09 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TesterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('element', models.CharField(max_length=3)),
                ('level', models.IntegerField(default=1)),
            ],
        ),
    ]