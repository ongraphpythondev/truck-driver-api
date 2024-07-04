# Generated by Django 5.0.6 on 2024-07-04 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('is_active', models.BooleanField(default=False)),
                ('is_trash', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255, null=True)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('speed', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('is_trash', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('driver_id', models.CharField(max_length=255, unique=True)),
                ('duty_status', models.CharField(choices=[('OFF', 'Off duty'), ('SB', 'Sleeper berth'), ('ON', 'On duty not driving'), ('D', 'Driving'), ('YM', 'Yard moves'), ('PC', 'Authorized personal use of CMV')], max_length=3, null=True)),
                ('duty_status_start_time', models.DateTimeField(null=True)),
                ('shift_work_minutes', models.BigIntegerField()),
                ('shift_drive_minutes', models.BigIntegerField()),
                ('cycle_work_minutes', models.BigIntegerField()),
                ('max_shift_work_minutes', models.BigIntegerField()),
                ('max_shift_drive_minutes', models.BigIntegerField()),
                ('max_cycle_work_minutes', models.BigIntegerField()),
                ('home_terminal_time_zone_windows', models.CharField(max_length=255)),
                ('home_terminal_time_zone_iana', models.CharField(max_length=255)),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='app.truck', verbose_name='Truck')),
            ],
            options={
                'db_table': 'drivers',
            },
        ),
    ]
