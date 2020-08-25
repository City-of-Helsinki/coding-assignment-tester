# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-08-25 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassedTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_input', models.TextField()),
                ('test_output', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_time', models.DateTimeField(help_text='When this answer to coding assignment was tested as working')),
                ('submission_endpoint_address', models.URLField(help_text='The address (endpoint) where this answer was tested', max_length=2048)),
                ('applicant_address', models.URLField(help_text="Applicant's contact info (mailto: or tel: URL)", max_length=2048)),
                ('submission_code_address', models.URLField(help_text='Address where the code implementing the submission can be found', max_length=2048)),
            ],
        ),
        migrations.AddField(
            model_name='passedtest',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.Submission'),
        ),
    ]
