# Generated by Django 2.0.13 on 2019-06-29 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ycms', '0007_auto_20190629_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='username',
            field=models.CharField(max_length=5),
        ),
    ]
