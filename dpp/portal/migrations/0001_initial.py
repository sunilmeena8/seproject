# Generated by Django 2.2 on 2019-11-18 06:37

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
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('specialization', models.CharField(max_length=40, null=True)),
                ('name', models.CharField(max_length=40, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('occupation', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FreeTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t0_1', models.BooleanField()),
                ('t1_2', models.BooleanField()),
                ('t2_3', models.BooleanField()),
                ('t3_4', models.BooleanField()),
                ('t4_5', models.BooleanField()),
                ('t5_6', models.BooleanField()),
                ('t6_7', models.BooleanField()),
                ('t7_8', models.BooleanField()),
                ('t8_9', models.BooleanField()),
                ('t9_10', models.BooleanField()),
                ('t10_11', models.BooleanField()),
                ('t11_12', models.BooleanField()),
                ('t12_13', models.BooleanField()),
                ('t13_14', models.BooleanField()),
                ('t14_15', models.BooleanField()),
                ('t15_16', models.BooleanField()),
                ('t16_17', models.BooleanField()),
                ('t17_18', models.BooleanField()),
                ('t18_19', models.BooleanField()),
                ('t19_20', models.BooleanField()),
                ('t20_21', models.BooleanField()),
                ('t21_22', models.BooleanField()),
                ('t22_23', models.BooleanField()),
                ('t23_24', models.BooleanField()),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10)),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Doctor')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10)),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Doctor')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Patient')),
            ],
        ),
    ]
