# Generated by Django 2.0.6 on 2018-06-05 23:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Lastname')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='Firsttname')),
                ('mid_name', models.CharField(blank=True, max_length=100, verbose_name='Midname')),
                ('about', models.TextField(blank=True, default='Some information', verbose_name='Information about You')),
                ('image', models.ImageField(blank=True, null=True, upload_to='userprofile', verbose_name='Avatar')),
                ('email', models.EmailField(default=' ', max_length=254)),
                ('phone_number', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000000000), django.core.validators.MinValueValidator(0)], verbose_name='Phone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]