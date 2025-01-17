# Generated by Django 2.1.7 on 2019-06-10 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_no', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='DeptEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='humanresource.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='DeptManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('dept_no', models.OneToOneField(db_column='dept_no', on_delete=django.db.models.deletion.DO_NOTHING, to='humanresource.Departments')),
            ],
            options={
                'db_table': 'dept_manager',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.AutoField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField(null=True)),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('hire_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'employees',
                'ordering': ['hire_date'],
            },
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(null=True)),
                ('advance', models.PositiveIntegerField(null=True)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='salary', to='humanresource.Employee')),
            ],
            options={
                'db_table': 'salaries',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='title', to='humanresource.Employee')),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.AddField(
            model_name='deptmanager',
            name='emp_no',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, to='humanresource.Employee'),
        ),
        migrations.AddField(
            model_name='deptemployee',
            name='emp_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='humanresource.Employee'),
        ),
        migrations.AlterUniqueTogether(
            name='salaries',
            unique_together={('emp_no', 'from_date')},
        ),
        migrations.AlterUniqueTogether(
            name='deptmanager',
            unique_together={('emp_no', 'dept_no')},
        ),
        migrations.AlterUniqueTogether(
            name='deptemployee',
            unique_together={('emp_no', 'dept_no')},
        ),
    ]
