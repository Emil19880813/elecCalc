# Generated by Django 2.2.10 on 2020-04-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0018_auto_20200403_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='voltage',
            field=models.CharField(choices=[('0', '0.23'), ('1', '0.4'), ('2', '15')], default=1, max_length=25),
        ),
    ]
