# Generated by Django 2.0.13 on 2019-06-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ycms', '0010_auto_20190629_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]