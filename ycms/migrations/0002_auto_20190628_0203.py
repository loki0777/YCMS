# Generated by Django 2.0.13 on 2019-06-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ycms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_details',
            old_name='event_date',
            new_name='eDate',
        ),
        migrations.RenameField(
            model_name='event_details',
            old_name='event_type',
            new_name='eType',
        ),
        migrations.AddField(
            model_name='event_details',
            name='vAddress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
