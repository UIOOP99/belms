# Generated by Django 3.1.4 on 2021-01-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment_answer',
            old_name='File_id',
            new_name='file_id',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assignment_answer',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
