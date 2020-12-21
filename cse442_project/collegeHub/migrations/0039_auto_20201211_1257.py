# Generated by Django 3.1.2 on 2020-12-11 12:57

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeHub', '0038_auto_20201208_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/BlueHead.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
