# Generated by Django 5.1.1 on 2024-09-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='job_end_date',
        ),
        migrations.AddField(
            model_name='name',
            name='role',
            field=models.CharField(default='Intern', max_length=60),
            preserve_default=False,
        ),
    ]
