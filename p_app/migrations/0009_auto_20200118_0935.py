# Generated by Django 2.2.6 on 2020-01-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0008_auto_20200118_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
