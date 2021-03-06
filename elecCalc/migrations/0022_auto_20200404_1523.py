# Generated by Django 2.2.10 on 2020-04-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0021_auto_20200403_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cable',
            name='cable_cross_section',
            field=models.CharField(choices=[('1.5', '1.5'), ('2.5', '2.5'), ('4', '4'), ('6', '6'), ('10', '10'), ('16', '16'), ('25', '25'), ('35', '35'), ('50', '50'), ('70', '70'), ('95', '95'), ('120', '120'), ('150', '150'), ('185', '185'), ('240', '240')], default='2.5', max_length=6),
        ),
        migrations.AlterField(
            model_name='cable',
            name='cable_routing',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F1', 'F1'), ('F2', 'F2'), ('F3', 'F3'), ('G', 'G')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='cable',
            name='insulation',
            field=models.CharField(choices=[('PVC', 'PVC'), ('XLPE', 'XLPE')], default='PVC', max_length=6),
        ),
        migrations.AlterField(
            model_name='cable',
            name='material',
            field=models.CharField(choices=[('Al', 'Al'), ('Cu', 'Cu')], default='Cu', max_length=6),
        ),
        migrations.AlterField(
            model_name='protectiondevices',
            name='current',
            field=models.CharField(choices=[('6', '6'), ('10', '10'), ('16', '16'), ('20', '20'), ('25', '25'), ('32', '32'), ('40', '40'), ('50', '50'), ('80', '80'), ('100', '100'), ('125', '125'), ('160', '160'), ('200', '200'), ('315', '315'), ('400', '400'), ('630', '630'), ('1000', '1000'), ('1600', '1600'), ('2000', '2000'), ('2500', '2500'), ('3200', '3200'), ('4000', '4000')], default='16', max_length=12),
        ),
        migrations.AlterField(
            model_name='protectiondevices',
            name='name',
            field=models.CharField(choices=[('WN', 'wyłącznik nadprądowy'), ('WS', 'wyłącznik selektywny'), ('WK', 'wyłącznik kompaktowy'), ('WP', 'wyłącznik powietrzny'), ('B', 'wkładka bezpiecznikowa')], default='WN', max_length=2),
        ),
        migrations.AlterField(
            model_name='protectiondevices',
            name='type',
            field=models.CharField(choices=[('B', 'B'), ('C', 'C'), ('D', 'D'), ('gG', 'gG'), ('Compact', 'Compact')], default='B', max_length=12),
        ),
    ]
