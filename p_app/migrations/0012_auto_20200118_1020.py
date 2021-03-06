# Generated by Django 2.2.6 on 2020-01-18 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0011_auto_20200118_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='p_app.Description'),
        ),
    ]
