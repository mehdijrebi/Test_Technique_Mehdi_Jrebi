# Generated by Django 3.1.6 on 2021-02-06 18:16

from django.db import migrations, models
import django.utils.timezone
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210206_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='file',
            name='pdf',
            field=models.FileField(null=True, upload_to=myapp.models.content_file_name),
        ),
    ]
