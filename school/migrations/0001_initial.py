# Generated by Django 2.2.7 on 2020-04-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schoolInfo',
            fields=[
                ('SchoolEIIN', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=100)),
                ('schoolAddress', models.CharField(max_length=100)),
                ('totalStudent', models.IntegerField()),
                ('totalTeacher', models.IntegerField()),
                ('attendance_percentage', models.IntegerField(default=1)),
                ('pass_percentage', models.IntegerField(default=1)),
            ],
        ),
    ]
