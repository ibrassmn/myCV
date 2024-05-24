# Generated by Django 5.0.4 on 2024-05-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0008_alter_skillleft_options_alter_skillright_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceLeft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('company_name', models.CharField(blank=True, default='', max_length=254, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, default='', max_length=254, verbose_name='Job Title')),
                ('job_location', models.CharField(blank=True, default='', max_length=254, verbose_name='Job_Location')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='End_Date')),
            ],
            options={
                'verbose_name': 'Experience Left',
                'verbose_name_plural': 'Experiences Left',
                'ordering': ('start_date',),
            },
        ),
    ]