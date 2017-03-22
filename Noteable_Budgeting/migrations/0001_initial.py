# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parents', models.DecimalField(decimal_places=2, max_digits=10)),
                ('jobs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('grants_bursaries_scholarships', models.DecimalField(decimal_places=2, max_digits=10)),
                ('student_loan', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('travel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bills', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_outcome', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
