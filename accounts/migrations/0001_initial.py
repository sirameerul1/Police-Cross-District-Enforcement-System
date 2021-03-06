# Generated by Django 3.0.5 on 2021-11-17 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('ic', models.IntegerField(null=True)),
                ('Address', models.CharField(max_length=200, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car', models.CharField(max_length=30, null=True)),
                ('plate', models.CharField(max_length=10, null=True)),
                ('date_leaving', models.DateField(null=True)),
                ('date_arrive', models.DateField(null=True)),
                ('origin', models.CharField(max_length=25, null=True)),
                ('destination', models.CharField(max_length=25, null=True)),
                ('reason', models.CharField(max_length=500, null=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('name_passenger1', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger1', models.IntegerField(blank=True, null=True)),
                ('image_ic1', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('name_passenger2', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger2', models.IntegerField(blank=True, null=True)),
                ('image_ic2', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('name_passenger3', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger3', models.IntegerField(blank=True, null=True)),
                ('image_ic3', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('name_passenger4', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger4', models.IntegerField(blank=True, null=True)),
                ('image_ic4', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('DECLINED', 'DECLINED'), ('PENDING', 'PENDING')], default='PENDING', max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user_driver')),
            ],
        ),
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car', models.CharField(max_length=30, null=True)),
                ('plate', models.CharField(max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_leaving', models.DateField(null=True)),
                ('date_arrive', models.DateField(null=True)),
                ('origin', models.CharField(max_length=25, null=True)),
                ('destination', models.CharField(max_length=25, null=True)),
                ('reason', models.CharField(max_length=500, null=True)),
                ('name_passenger1', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger1', models.IntegerField(blank=True, null=True)),
                ('name_passenger2', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger2', models.IntegerField(blank=True, null=True)),
                ('name_passenger3', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger3', models.IntegerField(blank=True, null=True)),
                ('name_passenger4', models.CharField(blank=True, max_length=200, null=True)),
                ('ic_passenger4', models.IntegerField(blank=True, null=True)),
                ('statusapplication', models.CharField(choices=[('APPROVED', 'APPROVED'), ('DECLINED', 'DECLINED'), ('PENDING', 'PENDING')], default='PENDING', max_length=500, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user_driver')),
            ],
        ),
    ]
