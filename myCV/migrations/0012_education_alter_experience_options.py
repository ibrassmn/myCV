# Generated by Django 5.0.4 on 2024-05-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0011_experience_job_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('school_name', models.CharField(blank=True, default='', max_length=254, verbose_name='School Name')),
                ('major', models.CharField(blank=True, default='', max_length=254, verbose_name='Major')),
                ('department', models.CharField(blank=True, default='', max_length=254, verbose_name='Job_Location')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='End_Date')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Education',
                'ordering': ('-start_date',),
            },
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('-start_date',), 'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
    ]
