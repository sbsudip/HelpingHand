# Generated by Django 3.0.7 on 2020-08-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0004_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='allowed',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0),
        ),
    ]