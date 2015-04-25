# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('address_header', models.CharField(max_length=100)),
                ('name_surname', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('post_code', models.IntegerField()),
                ('cell_phone', models.IntegerField()),
                ('phone', models.IntegerField(blank=True)),
                ('identification_number', models.IntegerField()),
                ('user', models.OneToOneField(to='user.User')),
            ],
        ),
    ]
