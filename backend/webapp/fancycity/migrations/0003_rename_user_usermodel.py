# Generated by Django 4.0.3 on 2022-03-19 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fancycity", "0002_user_address_user_birthdate_user_firstname_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="UserModel",
        ),
    ]
