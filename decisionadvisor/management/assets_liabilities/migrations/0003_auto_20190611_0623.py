# Generated by Django 2.1.7 on 2019-06-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_liabilities', '0002_auto_20190611_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liabilities',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
