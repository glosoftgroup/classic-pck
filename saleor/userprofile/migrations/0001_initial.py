# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-30 09:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import saleor.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='fullname')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='employee status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_new_code', models.BooleanField(default=True, verbose_name='new code checker')),
                ('send_mail', models.BooleanField(default=True, verbose_name='send mail')),
                ('code', models.CharField(blank=True, default='', max_length=255, null=True, unique=True, verbose_name='code')),
                ('rest_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='rest code')),
                ('job_title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='job title')),
                ('nid', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='employee')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'permissions': [('generate_code', 'Can generate Code')],
            },
            bases=(models.Model, saleor.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=256, verbose_name='given name')),
                ('last_name', models.CharField(blank=True, max_length=256, verbose_name='family name')),
                ('company_name', models.CharField(blank=True, max_length=256, verbose_name='company or organization')),
                ('street_address_1', models.CharField(blank=True, max_length=256, verbose_name='address')),
                ('street_address_2', models.CharField(blank=True, max_length=256, verbose_name='address')),
                ('city', models.CharField(blank=True, max_length=256, verbose_name='city')),
                ('city_area', models.CharField(blank=True, max_length=128, verbose_name='district')),
                ('postal_code', models.CharField(blank=True, max_length=20, verbose_name='postal code')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
                ('country_area', models.CharField(blank=True, max_length=128, verbose_name='state or province')),
                ('phone', models.CharField(blank=True, max_length=30, unique=True, verbose_name='phone number')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('national_id', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('date_recorded', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('date_joined', models.CharField(blank=True, max_length=100, null=True)),
                ('work_time', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(default='employee/user.png', upload_to='employee')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('pin', models.CharField(blank=True, max_length=100, null=True)),
                ('account', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_branch', models.CharField(blank=True, max_length=100, null=True)),
                ('nhif', models.CharField(blank=True, max_length=100, null=True)),
                ('nssf', models.CharField(blank=True, max_length=100, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=100, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('action', models.CharField(blank=True, max_length=100, null=True)),
                ('now', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=datetime.date.today)),
                ('crud', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(blank=True, to='userprofile.Address', verbose_name='addresses'),
        ),
        migrations.AddField(
            model_name='user',
            name='default_billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='userprofile.Address', verbose_name='default billing address'),
        ),
        migrations.AddField(
            model_name='user',
            name='default_shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='userprofile.Address', verbose_name='default shipping address'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
