# Generated by Django 3.0.8 on 2020-07-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medbase', '0006_auto_20200727_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='desciprion',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
