# Generated by Django 2.2.10 on 2020-03-21 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(choices=[(0, 'Al'), (1, 'Cu')], default=1, max_length=6)),
                ('insulation', models.CharField(choices=[(0, 'PVC'), (1, 'XLPE')], default=0, max_length=6)),
                ('cable_cross_section', models.DecimalField(choices=[(0, 1.5), (1, 2.5), (2, 4), (3, 6), (4, 10), (5, 16), (6, 25), (7, 35), (8, 50), (9, 70), (10, 95), (11, 125), (12, 150), (13, 185), (14, 240)], decimal_places=1, default=1, max_digits=4)),
                ('capacity', models.DecimalField(decimal_places=1, max_digits=4)),
                ('cable_routing', models.CharField(choices=[(0, 'A1'), (1, 'A2'), (2, 'B1'), (3, 'B2'), (4, 'C'), (5, 'D'), (6, 'E'), (7, 'F1'), (8, 'F2'), (9, 'F3'), (10, 'G')], default=1, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='GroupReceiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('LI', 'OŚWIETLENIE'), ('WM', 'ZESPOŁY WIELOMASZYNOWE'), ('SI', 'SILNIK ELEKTRYCZNY'), ('ENE', 'URZĄDZENIA ENERGOELEKTRONICZNE'), ('PRS', 'URZĄDZENIA PROSTOWNIKOWE'), ('SPA', 'URZĄDZENIA SPAWALNICZE')], default='LI', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('voltage', models.DecimalField(choices=[(0, 0.23), (1, 0.4), (2, 15)], decimal_places=2, default=1, max_digits=3)),
                ('power', models.DecimalField(decimal_places=2, max_digits=6)),
                ('power_factor', models.DecimalField(decimal_places=2, default=0.93, max_digits=3)),
                ('cable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='elecCalc.Cable')),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='elecCalc.GroupReceiver')),
            ],
        ),
        migrations.CreateModel(
            name='ProtectionDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(0, 'B'), (1, 'C'), (2, 'D'), (3, 'gG'), (4, 'Compact')], default=0, max_length=32)),
                ('current', models.SmallIntegerField(choices=[(0, 10), (1, 16), (2, 25), (3, 40), (4, 50), (5, 80), (6, 100), (7, 125), (8, 160), (9, 200), (10, 250), (11, 315), (12, 400), (13, 630), (14, 800), (15, 1000), (16, 1250), (17, 1600), (18, 2500), (19, 4000)], default=0)),
                ('receivers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='elecCalc.Receiver')),
            ],
        ),
    ]
