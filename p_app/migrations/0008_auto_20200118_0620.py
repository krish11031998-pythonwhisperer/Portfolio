# Generated by Django 2.2.6 on 2020-01-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0007_auto_20200118_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='img_num',
            new_name='img_url',
        ),
        migrations.AddField(
            model_name='project',
            name='headline',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name of the project'),
        ),
    ]
