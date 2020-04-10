from django.db import models

# Create your models here.


OVERLOAD_FACTOR_CHOICES = (
    ('1.2', '1.2'),
    ('1.45', '1.45'),
    ('1.6', '1.6'),
    ('1.9', '1.9'),
)

CABLE_CROSS_SECTION_CHOICES = (
    ('1.5', '1.5'),
    ('2.5', '2.5'),
    ('4', '4'),
    ('6', '6'),
    ('10', '10'),
    ('16', '16'),
    ('25', '25'),
    ('35', '35'),
    ('50', '50'),
    ('70', '70'),
    ('95', '95'),
    ('125', '125'),
    ('150', '150'),
    ('185', '185'),
    ('240', '240'),
)

CABLE_INSULATION_CHOICES = (
    ('PVC', 'PVC'),
    ('XLPE', 'XLPE'),
)

CABLE_TYPE_CHOICES = (
    ('Al', 'Al'),
    ('Cu', 'Cu'),
)

ROUTING_CHOICES = (
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F1', 'F1'),
    ('F2', 'F2'),
    ('F3', 'F3'),
    ('G', 'G'),
)

OVERCURRENT_TYPE_CHOICES = (
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('gG', 'gG'),
    ('Compact', 'Compact'),
)

CURRENT_CHOICES = (
    ('10', '10'),
    ('16', '16'),
    ('25', '25'),
    ('40', '40'),
    ('50', '50'),
    ('80', '80'),
    ('100', '100'),
    ('125', '125'),
    ('160', '160'),
    ('200', '200'),
    ('250', '250'),
    ('315', '315'),
    ('400', '400'),
    ('630', '630'),
    ('800', '800'),
    ('1000', '1000'),
    ('1250', '1250'),
    ('1600', '1600'),
    ('2500', '2500'),
    ('4000', '4000'),
)

DEVICE_NAME_CHOICES = (
    ('WN', 'wyłącznik nadprądowy'),
    ('WS', 'wyłącznik selektywny'),
    ('WK', 'wyłącznik kompaktowy'),
    ('WP', 'wyłącznik powietrzny'),
    ('B', 'wkładka bezpiecznikowa'),
)

POWER_TRAFO_CHOICES = (
    ('100', '100'),
    ('160', '160'),
    ('200', '200'),
    ('250', '250'),
    ('315', '315'),
    ('400', '400'),
    ('500', '500'),
    ('630', '630'),
    ('800', '800'),
    ('1000', '1000'),
    ('1250', '1250'),
    ('1600', '1600'),
    ('2000', '2000'),
    ('2500', '2500'),
    ('3150', '3150'),
)

class Cable(models.Model):
    material = models.CharField(max_length=6, choices=CABLE_TYPE_CHOICES, default='Cu')  # materiał Cu Al
    insulation = models.CharField(max_length=6, choices=CABLE_INSULATION_CHOICES, default='PVC')  # izolacja
    cable_cross_section = models.CharField(max_length=6, choices=CABLE_CROSS_SECTION_CHOICES, default='2.5')  # przekrój
    capacity = models.DecimalField(max_digits=4, decimal_places=1)  # obciążalnosc długotrwała
    cable_routing = models.CharField(max_length=2, choices=ROUTING_CHOICES, default='E')  # sposób ułożenia

    def __str__(self):
        return f'{self.get_material_display()}/{self.get_insulation_display()}/{self.get_cable_cross_section_display()}/' \
               f'{self.get_cable_routing_display()}'


class ProtectionDevices(models.Model):
    name = models.CharField(max_length=2, choices=DEVICE_NAME_CHOICES, default='WN')
    type = models.CharField(max_length=12, choices=OVERCURRENT_TYPE_CHOICES, default='B')  # typ zabezpieczenia
    current = models.CharField(max_length=6, choices=CURRENT_CHOICES, default='16')  # amperaż zabezpieczenia
    cable = models.ForeignKey(Cable, on_delete=models.SET_NULL, null=True, blank=True, related_name="devices")

    def __str__(self):
        return f"{self.get_type_display()}/{self.get_current_display()}A"

class Transformer(models.Model):
    power = models.IntegerField(choices=POWER_TRAFO_CHOICES, default=630)
    load_loss = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True) #straty ociążeniowe
    no_load_loss = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True) #straty jałowe
    reactance = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    resistance = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    device = models.ForeignKey(ProtectionDevices, on_delete=models.SET_NULL, null=True, blank=True, related_name="transformers")

    def __str__(self):
        return f"Trafo:{self.power}A"

class CalculationResult(models.Model):
    position = models.IntegerField()
    cir_number = models.CharField(max_length=12)
    cir_name = models.CharField(max_length=64)
    cir_voltage = models.DecimalField(max_digits=4, decimal_places=2)
    cir_power = models.DecimalField(max_digits=6, decimal_places=2)
    cir_cos_fi = models.DecimalField(max_digits=3, decimal_places=2)
    cir_current = models.DecimalField(max_digits=6, decimal_places=2)
    cab_amount = models.IntegerField()
    core_amount = models.IntegerField()
    cab_routing = models.CharField(max_length=2)
    cab_insulation = models.CharField(max_length=4)
    cab_material = models.CharField(max_length=2)
    cab_cable_cross_section = models.DecimalField(max_digits=4, decimal_places=1)
    cab_length = models.IntegerField()
    cab_i_dd = models.DecimalField(max_digits=4, decimal_places=1)
    cab_kc_factor = models.DecimalField(max_digits=3, decimal_places=2)
    cab_i_z = models.DecimalField(max_digits=4, decimal_places=1)
    dev_type = models.CharField(max_length=12)
    dev_current = models.IntegerField(default=2)
    dev_kr_factor = models.DecimalField(max_digits=3, decimal_places=2)
    dev_i_r = models.DecimalField(max_digits=6, decimal_places=2)
    dev_k2_factor = models.DecimalField(max_digits=5, decimal_places=2)
    dev_i_2 = models.DecimalField(max_digits=6, decimal_places=2)
    conditions = models.CharField(max_length=6)
    cab_vol_drop = models.DecimalField(max_digits=4, decimal_places=2)
