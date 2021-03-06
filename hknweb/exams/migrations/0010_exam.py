# Generated by Django 2.2.8 on 2020-04-06 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20190421_2337_squashed_0012_auto_20191001_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Department')),
            ],
        ),
    ]
