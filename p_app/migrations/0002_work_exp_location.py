# Generated by Django 2.2.6 on 2020-01-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_exp',
            name='location',
            field=models.CharField(max_length=75, null=True),
        ),
    ]