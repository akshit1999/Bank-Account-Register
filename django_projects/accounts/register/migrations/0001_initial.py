# Generated by Django 3.1 on 2020-09-08 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(blank=True, max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50)),
                ('Address1', models.TextField(max_length=100)),
                ('Address2', models.TextField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('PinCode', models.IntegerField()),
                ('DOB', models.DateField()),
                ('ContactNumber', models.IntegerField()),
                ('Occupation', models.CharField(max_length=50)),
                ('docImage', models.FileField(upload_to='register/pictures')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountType', models.CharField(choices=[('Savings', 'Savings'), ('Current', 'Current')], max_length=50)),
                ('Currency', models.CharField(choices=[('Rupee', 'Rupee'), ('US Dollar', 'US Dollar'), ('Euro', 'Euro'), ('Pound', 'Pound')], max_length=50)),
                ('AccountNumber', models.CharField(max_length=120)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
