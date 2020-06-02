# Generated by Django 3.0.6 on 2020-05-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_student_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
