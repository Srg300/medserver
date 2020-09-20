# Generated by Django 3.0.8 on 2020-07-30 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medbase', '0015_auto_20200729_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='pill',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='pill', to='medbase.Pill'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drug',
            name='title',
            field=models.CharField(max_length=100, verbose_name='назначение'),
        ),
    ]
