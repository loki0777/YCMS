# Generated by Django 2.0.13 on 2019-06-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ycms', '0003_auto_20190628_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_details',
            name='eDate',
            field=models.DateField(null=True),
        ),
    ]