# Generated by Django 5.1.7 on 2025-03-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0002_alter_uploadedfile_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedfile",
            name="file",
            field=models.FileField(upload_to="uploads/"),
        ),
    ]
