# Generated by Django 2.1.7 on 2019-06-12 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20190612_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='balance',
            new_name='amount',
        ),
    ]
