# Generated by Django 3.0.8 on 2020-07-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medbase', '0021_auto_20200730_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pill',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название лекарства'),
        ),
    ]