# Generated by Django 3.0.4 on 2020-12-08 20:41

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
                ('start_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='assignment_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('course_id', models.TextField()),
                ('File_id', models.TextField()),
                ('description', models.TextField(default='')),
                ('date_of_upload', models.DateTimeField()),
            ],
        ),
    ]