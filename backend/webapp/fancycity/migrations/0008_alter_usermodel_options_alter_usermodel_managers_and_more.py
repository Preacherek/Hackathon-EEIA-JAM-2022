# Generated by Django 4.0.3 on 2022-03-19 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fancycity", "0007_alter_usermodel_username"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usermodel",
            options={},
        ),
        migrations.AlterModelManagers(
            name="usermodel",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="admin",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="staff",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="user_permissions",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="username",
        ),
    ]
