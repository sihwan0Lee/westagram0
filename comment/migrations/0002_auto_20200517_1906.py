# Generated by Django 3.0.5 on 2020-05-17 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]