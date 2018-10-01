# Generated by Django 2.0.1 on 2018-08-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirurlmodel',
            name='Shortcode',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='kirurlmodel',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
