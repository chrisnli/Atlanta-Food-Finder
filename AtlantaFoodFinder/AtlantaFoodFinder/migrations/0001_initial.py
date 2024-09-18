# Generated by Django 5.1.1 on 2024-09-16 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('place_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=512)),
                ('contact_info', models.CharField(max_length=512)),
                ('cuisine_type', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('user', models.CharField(max_length=128)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=1024)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AtlantaFoodFinder.location')),
            ],
        ),
    ]
