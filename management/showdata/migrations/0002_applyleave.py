# Generated by Django 2.2.5 on 2020-01-01 02:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyleave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave', models.CharField(choices=[('CL', 'CL'), ('EL', 'EL'), ('PL', 'PL'), ('TL', 'TL')], default='CL', max_length=10)),
                ('holidayfrom', models.DateField(default=datetime.date.today)),
                ('holidayto', models.DateField(default=datetime.date.today)),
                ('detail', models.TextField()),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
