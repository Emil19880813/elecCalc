# Generated by Django 2.2.10 on 2020-04-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0030_auto_20200407_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculationresult',
            name='cable',
        ),
        migrations.RemoveField(
            model_name='calculationresult',
            name='device',
        ),
        migrations.AddField(
            model_name='calculationresult',
            name='cab_cable_cross_section',
            field=models.DecimalField(decimal_places=1, default='2.5', max_digits=4),
        ),
        migrations.AddField(
            model_name='calculationresult',
            name='cab_insulation',
            field=models.CharField(default='PVC', max_length=4),
        ),
        migrations.AddField(
            model_name='calculationresult',
            name='cab_material',
            field=models.CharField(default='Al', max_length=2),
        ),
        migrations.AddField(
            model_name='calculationresult',
            name='cab_routing',
            field=models.CharField(default='E', max_length=2),
        ),
        migrations.AddField(
            model_name='calculationresult',
            name='dev_current',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='calculationresult',
            name='dev_type',
            field=models.CharField(default='B', max_length=12),
        ),
    ]
