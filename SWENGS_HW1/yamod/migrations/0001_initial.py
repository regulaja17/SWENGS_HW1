# Generated by Django 2.2.6 on 2019-10-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('birthdate', models.DateField()),
                ('studies', models.CharField(choices=[('ima', 'Information Management'), ('geb', 'E-Health'), ('bau', 'Bauingenieurswesen')], max_length=3)),
            ],
        ),
    ]
