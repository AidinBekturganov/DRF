# Generated by Django 3.1.7 on 2021-05-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khata', '0004_auto_20210511_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.DateField(),
        ),
    ]
