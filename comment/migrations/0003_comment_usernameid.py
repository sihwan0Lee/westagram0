# Generated by Django 3.0.5 on 2020-05-22 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200521_1508'),
        ('comment', '0002_auto_20200517_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='usernameid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account'),
        ),
    ]
