# Generated by Django 2.2.5 on 2019-09-09 12:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gardens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.CharField(choices=[('imperial', 'imperial'), ('japanese', 'japanese'), ('stone', 'stone'), ('flower', 'flower'), ('other', 'other')], max_length=20)),
                ('rating', models.PositiveIntegerField()),
                ('free_entrance', models.BooleanField(default=False)),
                ('last_renewal', models.DateTimeField()),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
