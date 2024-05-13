# Generated by Django 5.0.4 on 2024-05-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0003_imagesettings_alter_generalsetting_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='The name of the general setting', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', help_text='The description of the general setting', max_length=254, verbose_name='Description')),
                ('file', models.FileField(blank=True, default='', upload_to='images/', verbose_name='Image')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Image Setting',
                'verbose_name_plural': 'Image Settings',
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='ImageSettings',
        ),
    ]