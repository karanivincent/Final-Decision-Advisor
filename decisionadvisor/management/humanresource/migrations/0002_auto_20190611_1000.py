# Generated by Django 2.1.7 on 2019-06-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humanresource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='ID',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.PositiveIntegerField(null=True),
        ),
    ]