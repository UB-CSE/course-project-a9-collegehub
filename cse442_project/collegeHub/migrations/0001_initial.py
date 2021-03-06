# Generated by Django 3.0.4 on 2020-10-13 19:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Section', max_length=30)),
                ('experiences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='collegeHub.Experiences')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile_pic', models.ImageField(blank=True, default='images/BlueHead.jpg', null=True, upload_to='images/')),
                ('bio', models.TextField(blank=True, default='')),
                ('bio_html', models.TextField(editable=False)),
                ('location', models.CharField(blank=True, default='', max_length=255)),
                ('occupation', models.CharField(blank=True, default='', max_length=255)),
                ('github', models.CharField(blank=True, default='', max_length=255)),
                ('instagram', models.CharField(blank=True, default='', max_length=255)),
                ('linkedin', models.CharField(blank=True, default='', max_length=255)),
                ('resume', models.FileField(blank=True, null=True, upload_to='files/')),
                ('quote', models.CharField(blank=True, default='', max_length=255)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='media/right-arrow.png', null=True, upload_to='media/')),
                ('description', models.CharField(default='This is what did', max_length=2000)),
                ('bullet_section', models.CharField(default='Bullet, points, are, great', max_length=200)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific', to='collegeHub.Section')),
            ],
        ),
        migrations.AddField(
            model_name='experiences',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='collegeHub.UserProfile'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='media/right-arrow.png', null=True, upload_to='media/')),
                ('location', models.CharField(default='NA', max_length=50, null=True)),
                ('certification_name', models.CharField(default='NA', max_length=50)),
                ('description', models.CharField(default='NA', max_length=280)),
                ('month', models.CharField(default='01', max_length=2)),
                ('year', models.CharField(default='9999', max_length=4)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='collegeHub.UserProfile')),
            ],
        ),
    ]
