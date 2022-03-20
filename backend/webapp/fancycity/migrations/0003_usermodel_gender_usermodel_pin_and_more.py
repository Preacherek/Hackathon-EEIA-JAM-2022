# Generated by Django 4.0.3 on 2022-03-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fancycity", "0002_remove_usermodel_dsf"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="gender",
            field=models.TextField(default="", max_length=128),
        ),
        migrations.AddField(
            model_name="usermodel",
            name="pin",
            field=models.TextField(default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="birthdate",
            field=models.TextField(
                default="", max_length=64, verbose_name="birth date"
            ),
        ),
    ]