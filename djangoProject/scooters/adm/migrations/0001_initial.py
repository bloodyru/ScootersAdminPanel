# Generated by Django 3.2.4 on 2021-06-24 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Soname', models.CharField(max_length=30, null=True)),
                ('DateOfCreation', models.DateTimeField(auto_now_add=True)),
                ('Bonuses', models.IntegerField(null=True)),
                ('Money', models.IntegerField(null=True)),
                ('TypeOperation', models.CharField(max_length=10, null=True)),
                ('Status', models.CharField(max_length=10, null=True)),
                ('DateOfOperation', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qr_code', models.IntegerField(unique=True)),
                ('Serial_number', models.IntegerField(unique=True)),
                ('Battery', models.IntegerField()),
                ('Price', models.CharField(max_length=30, null=True)),
                ('Power', models.CharField(max_length=30)),
                ('Trip', models.IntegerField(null=True)),
                ('Status', models.CharField(max_length=30, null=True)),
                ('Action', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Ico', models.ImageField(upload_to='')),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Soname', models.CharField(max_length=30, null=True)),
                ('Phone', models.CharField(max_length=30, null=True)),
                ('Email', models.EmailField(max_length=40)),
                ('IsActive', models.BooleanField(null=True)),
                ('LastActive', models.DateTimeField(auto_now=True)),
                ('DateOfRegistration', models.DateTimeField(auto_now_add=True)),
                ('PresentCode', models.CharField(max_length=30, null=True)),
                ('UserBalance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adm.balance')),
            ],
        ),
    ]
