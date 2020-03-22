# Generated by Django 2.2.10 on 2020-03-22 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0004_auto_20200322_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protectiondevices',
            name='receivers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='device', to='elecCalc.Receiver'),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='cable',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='elecCalc.Cable'),
        ),
    ]
