# Generated by Django 2.2.6 on 2020-01-18 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0004_auto_20200117_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='skill',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='p_app.Skill'),
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skills',
        ),
        migrations.AddField(
            model_name='skill',
            name='skills',
            field=models.ManyToManyField(to='p_app.input'),
        ),
    ]