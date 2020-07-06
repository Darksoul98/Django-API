# Generated by Django 3.0.8 on 2020-07-06 19:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=300)),
                ('tz', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('activity_periods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_activity.UserInfo')),
            ],
        ),
    ]
