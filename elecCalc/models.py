from django.db import models

# Create your models here.
group_receiver_choices = (
    ("LI", "OŚWIETLENIE"),
    ("WM", "ZESPOŁY WIELOMASZYNOWE"),
    ("SI", "SILNIK ELEKTRYCZNY"),
    ("ENE", "URZĄDZENIA ENERGOELEKTRONICZNE"),
    ("PRS", "URZĄDZENIA PROSTOWNIKOWE"),
    ("SPA", "URZĄDZENIA SPAWALNICZE"),
    ("GR", "GRZAŁKA"),
)

voltage_choices = (
    (0, 0.23),
    (1, 0.4),
    (2, 15),
)

cable_cross_section_choices = (
    (0, 1.5),
    (1, 2.5),
    (2, 4),
    (3, 6),
    (4, 10),
    (5, 16),
    (6, 25),
    (7, 35),
    (8, 50),
    (9, 70),
    (10, 95),
    (11, 125),
    (12, 150),
    (13, 185),
    (14, 240),
)

cable_insulation_choices = (
    (0, "PVC"),
    (1, "XLPE"),
)
cable_type_choices = (
    (0, "Al"),
    (1, "Cu"),
)
routing_choices = (
    (0, "A1"),
    (1, "A2"),
    (2, "B1"),
    (3, "B2"),
    (4, "C"),
    (5, "D"),
    (6, "E"),
    (7, "F1"),
    (8, "F2"),
    (9, "F3"),
    (10, "G"),
)

overcurrent_type_choices = (
    (0, "B"),
    (1, "C"),
    (2, "D"),
    (3, "gG"),
    (4, "Compact"),
)

current_choices = (
    (0, 10),
    (1, 16),
    (2, 25),
    (3, 40),
    (4, 50),
    (5, 80),
    (6, 100),
    (7, 125),
    (8, 160),
    (9, 200),
    (10, 250),
    (11, 315),
    (12, 400),
    (13, 630),
    (14, 800),
    (15, 1000),
    (16, 1250),
    (17, 1600),
    (18, 2500),
    (19, 4000),
)
device_name_choices = (
    (0, 'wyłącznik nadprądowy'),
    (1, 'wyłącznik selektywny'),
    (2, 'wyłącznik kompaktowy'),
    (3, 'wyłącznik powietrzny'),
    (4, 'wkładka bezpiecznikowa'),
)

class Cable(models.Model):
    material = models.IntegerField(choices=cable_type_choices, default=1)  # materiał Cu Al
    insulation = models.IntegerField(choices=cable_insulation_choices, default=0)  # izolacja
    cable_cross_section = models.DecimalField(max_digits=4, decimal_places=1, choices=cable_cross_section_choices, default=1)  # przekrój
    capacity = models.DecimalField(max_digits=4, decimal_places=1)  # obciążalnosc długotrwała
    cable_routing = models.IntegerField(choices=routing_choices, default=1)  # sposób ułożenia


    def __str__(self):
        return f'{self.get_material_display()}/{self.get_insulation_display()}/{self.get_cable_cross_section_display()}/' \
               f'{self.get_cable_routing_display()}'


class GroupReceiver(models.Model):
    name = models.CharField(max_length=64, choices=group_receiver_choices, default="LI", unique=True)

    def __str__(self):
        return f"{self.get_name_display()}"

class Receiver(models.Model):
    name = models.CharField(max_length=32)
    voltage = models.DecimalField(max_digits=3, decimal_places=2, choices=voltage_choices, default=1)
    power = models.DecimalField(max_digits=6, decimal_places=2)
    power_factor = models.DecimalField(max_digits=3, decimal_places=2, default=0.93)
    group = models.ForeignKey(GroupReceiver, on_delete=models.CASCADE, related_name="receivers")
    cable = models.ForeignKey(Cable, on_delete=models.SET_NULL, null=True, blank=True, related_name="receivers")

    def __str__(self):
        return f"{self.name} - {self.power}kW, {self.get_voltage_display()}kV"


class ProtectionDevices(models.Model):
    name = models.IntegerField(choices=device_name_choices, default=0)
    type = models.IntegerField(choices=overcurrent_type_choices, default=0)  # typ zabezpieczenia
    current = models.SmallIntegerField(choices=current_choices, default=0)  # amperaż zabezpieczenia
    receivers = models.ForeignKey(Receiver, on_delete=models.SET_NULL, blank=True, null=True, related_name="device")

    def __str__(self):
        return f"{self.get_type_display()}/{self.get_current_display()}A"

    class Meta:
        unique_together = ['type', 'current']
