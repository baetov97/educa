# Generated by Django 3.0.7 on 2020-06-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
