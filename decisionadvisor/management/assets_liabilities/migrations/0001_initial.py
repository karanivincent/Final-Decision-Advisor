# Generated by Django 2.1.7 on 2019-06-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('value', models.PositiveIntegerField()),
                ('purchase_date', models.DateField(null=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Liabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('amount', models.PositiveIntegerField()),
                ('DueDate', models.DateField(null=True)),
                ('StartDate', models.DateField(null=True)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
