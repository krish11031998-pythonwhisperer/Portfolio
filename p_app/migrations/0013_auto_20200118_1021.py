# Generated by Django 2.2.6 on 2020-01-18 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0012_auto_20200118_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='p_app.Description'),
        ),
    ]
