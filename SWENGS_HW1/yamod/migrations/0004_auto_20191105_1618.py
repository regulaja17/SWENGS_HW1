# Generated by Django 2.2.7 on 2019-11-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0003_auto_20191105_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='city',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='building',
            name='postal_code',
            field=models.TextField(),
        ),
    ]
