# Generated by Django 2.2.10 on 2020-03-29 17:33

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
                ('material', models.IntegerField(choices=[(0, 'Al'), (1, 'Cu')], default=1)),
                ('insulation', models.IntegerField(choices=[(0, 'PVC'), (1, 'XLPE')], default=0)),
                ('cable_cross_section', models.DecimalField(choices=[(0, 1.5), (1, 2.5), (2, 4), (3, 6), (4, 10), (5, 16), (6, 25), (7, 35), (8, 50), (9, 70), (10, 95), (11, 125), (12, 150), (13, 185), (14, 240)], decimal_places=1, default=1, max_digits=4)),
                ('capacity', models.DecimalField(decimal_places=1, max_digits=4)),
                ('cable_routing', models.IntegerField(choices=[(0, 'A1'), (1, 'A2'), (2, 'B1'), (3, 'B2'), (4, 'C'), (5, 'D'), (6, 'E'), (7, 'F1'), (8, 'F2'), (9, 'F3'), (10, 'G')], default=1)),
                ('amount', models.IntegerField(default=1)),
                ('core', models.IntegerField(default=1)),
                ('layer_factor', models.DecimalField(decimal_places=2, default=1, max_digits=3)),
                ('overload_factor', models.DecimalField(choices=[(0, 1.2), (1, 1.45), (2, 1.6), (3, 1.9)], decimal_places=2, default=0, max_digits=3)),
                ('length', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='GroupReceiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('LI', 'OŚWIETLENIE'), ('WM', 'ZESPOŁY WIELOMASZYNOWE'), ('SI', 'SILNIK ELEKTRYCZNY'), ('ENE', 'URZĄDZENIA ENERGOELEKTRONICZNE'), ('PRS', 'URZĄDZENIA PROSTOWNIKOWE'), ('SPA', 'URZĄDZENIA SPAWALNICZE'), ('GR', 'GRZAŁKA')], default='LI', max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circuit_number', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=32)),
                ('voltage', models.DecimalField(choices=[(0, 0.23), (1, 0.4), (2, 15)], decimal_places=2, default=1, max_digits=3)),
                ('power', models.DecimalField(decimal_places=2, max_digits=6)),
                ('power_factor', models.DecimalField(decimal_places=2, default=0.93, max_digits=3)),
                ('cable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receivers', to='elecCalc.Cable')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receivers', to='elecCalc.GroupReceiver')),
            ],
        ),
        migrations.CreateModel(
            name='ProtectionDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'wyłącznik nadprądowy'), (1, 'wyłącznik selektywny'), (2, 'wyłącznik kompaktowy'), (3, 'wyłącznik powietrzny'), (4, 'wkładka bezpiecznikowa')], default=0)),
                ('type', models.IntegerField(choices=[(0, 'B'), (1, 'C'), (2, 'D'), (3, 'gG'), (4, 'Compact')], default=0)),
                ('current', models.SmallIntegerField(choices=[(0, 10), (1, 16), (2, 25), (3, 40), (4, 50), (5, 80), (6, 100), (7, 125), (8, 160), (9, 200), (10, 250), (11, 315), (12, 400), (13, 630), (14, 800), (15, 1000), (16, 1250), (17, 1600), (18, 2500), (19, 4000)], default=0)),
                ('off_time', models.DecimalField(decimal_places=1, default=5, max_digits=2)),
                ('receivers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='device', to='elecCalc.Receiver')),
            ],
        ),
    ]
