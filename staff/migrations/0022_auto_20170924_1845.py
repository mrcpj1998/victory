# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('staff', '0021_auto_20170921_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='child_record',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='drivers_licence',
            field=models.ManyToManyField(blank=True, to='staff.DriversLicenceCategories'),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='sock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.Sock'),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='tshirt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.TShirt'),
        ),
    ]