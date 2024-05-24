# Generated by Django 5.0.4 on 2024-05-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0016_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='certificate_tag',
            field=models.CharField(blank=True, default='', help_text='The name of the general setting', max_length=254, verbose_name='Name'),
        ),
    ]