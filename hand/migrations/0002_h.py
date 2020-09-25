# Generated by Django 3.0.7 on 2020-08-10 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='h',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=500)),
                ('location', models.URLField(max_length=5000)),
                ('image', models.ImageField(upload_to='hospital')),
                ('contact_info', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=1000)),
                ('no_of_doctor', models.IntegerField()),
                ('no_of_beds_available', models.IntegerField()),
                ('corona', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
