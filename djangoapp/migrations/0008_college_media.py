# Generated by Django 3.0.6 on 2020-06-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_auto_20200610_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='media',
            field=models.CharField(choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], default='Audio', max_length=10),
        ),
    ]
