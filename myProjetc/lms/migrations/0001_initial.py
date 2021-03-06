# Generated by Django 3.1.4 on 2020-12-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('course_id', models.TextField()),
                ('file_id', models.TextField()),
                ('description', models.TextField(default='')),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('course_id', models.TextField()),
                ('File_id', models.TextField()),
                ('homework_number_id', models.TextField()),
                ('description', models.TextField(default='')),
                ('date_of_upload', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('course_id', models.TextField()),
                ('msg', models.TextField(default='')),
                ('date_of_send', models.DateField()),
            ],
        ),
    ]
