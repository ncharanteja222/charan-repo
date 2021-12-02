# Generated by Django 3.2.3 on 2021-06-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30, null=True)),
                ('emp_num', models.IntegerField(null=True)),
                ('emp_details', models.CharField(max_length=60, null=True)),
                ('emp_address', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]