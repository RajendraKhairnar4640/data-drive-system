# Generated by Django 5.1.4 on 2024-12-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0003_alter_file_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
