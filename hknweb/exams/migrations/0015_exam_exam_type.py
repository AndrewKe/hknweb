# Generated by Django 2.2.8 on 2020-04-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0014_auto_20200405_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(default='Mideterm 1', max_length=255),
        ),
    ]
