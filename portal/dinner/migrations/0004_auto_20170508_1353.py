# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0003_food_foodday'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodDay', models.TextField()),
            ],
            options={
                'db_table': 'food_day',
            },
        ),
        migrations.AlterField(
            model_name='food',
            name='foodDay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.FoodDay'),
        ),
    ]
