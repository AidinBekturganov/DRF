# Generated by Django 3.1.7 on 2021-05-04 05:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('year', models.DateTimeField()),
                ('area', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('excerpt', models.TextField(null=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
