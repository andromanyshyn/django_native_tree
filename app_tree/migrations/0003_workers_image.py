# Generated by Django 4.1.7 on 2023-03-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tree', '0002_alter_workers_employment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='workers_images'),
        ),
    ]