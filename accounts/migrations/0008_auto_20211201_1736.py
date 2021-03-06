# Generated by Django 3.0.5 on 2021-12-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_status_officername'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_driver',
            name='vaccination_status_driver',
            field=models.CharField(choices=[('Default', 'Default'), ('No Vaccinate', 'No Vaccinate'), ('First Dose', 'First Dose'), ('Second Dose (Partial)', 'Second Dose (Partial)'), ('Second Dose (Full)', 'Second Dose (Full)')], default='Default', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='officername',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
