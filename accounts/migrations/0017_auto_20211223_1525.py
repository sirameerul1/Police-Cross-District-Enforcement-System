# Generated by Django 3.0.5 on 2021-12-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20211223_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_driver',
            name='Address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user_driver',
            name='Phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_driver',
            name='gender',
            field=models.CharField(blank=True, choices=[('Gender', 'Gender'), ('Male', 'Male'), ('Female', 'Female')], default='gender', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user_driver',
            name='ic',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
