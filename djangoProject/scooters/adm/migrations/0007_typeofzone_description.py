# Generated by Django 3.2.4 on 2021-12-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0006_typeofzone_maxspeed'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofzone',
            name='Description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
