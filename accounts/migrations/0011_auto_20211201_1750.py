# Generated by Django 3.0.5 on 2021-12-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211201_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='vaccination_pdf_passenger1',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='status',
            name='vaccination_pdf_passenger2',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='status',
            name='vaccination_pdf_passenger3',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='status',
            name='vaccination_pdf_passenger4',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user_driver',
            name='vaccination_pdf',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
