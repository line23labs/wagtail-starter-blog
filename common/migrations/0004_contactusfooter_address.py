# Generated by Django 4.1.7 on 2023-06-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_alter_contactusfooter_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactusfooter",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
    ]
