# Generated by Django 3.0.4 on 2020-10-26 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeHub', '0009_auto_20201025_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='certification_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.CharField(blank=True, default='', max_length=280),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
