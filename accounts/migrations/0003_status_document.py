# Generated by Django 3.0.5 on 2021-11-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_status_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='document',
            field=models.FileField(default=121, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
