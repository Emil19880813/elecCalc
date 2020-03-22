from django import forms
from elecCalc.models import Receiver, GroupReceiver, Cable, ProtectionDevices

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        exclude = ['cable']

class GroupReceiverForm(forms.ModelForm):
    class Meta:
        model = GroupReceiver
        fields = '__all__'

class CableForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = '__all__'

class ProtectionDevicesForm(forms.ModelForm):
    class Meta:
        model = ProtectionDevices
        exclude = ['receivers']

class ReceiverResultForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=GroupReceiver.objects.all())
    power_factor = forms.DecimalField(max_digits=3, decimal_places=2, min_value=0.1, max_value=1)

    class Meta:
        model = Receiver
        fields = ('group', 'name', 'voltage', 'power', 'power_factor',)
        labels = {
            'group': 'grupa odbiorów',
            'name': 'nazwa',
            'voltage': 'napięcie',
            'power': 'moc',
            'power_factor': 'współczynnik mocy',
        }

        help_texts = {
            'voltage': '[kV]',
        }

class CableResultForm(forms.ModelForm):

    overload_factor_choices = (
        (0, 1.2),
        (1, 1.45),
        (2, 1.6),
        (3, 1.9),
    )
    amount = forms.IntegerField(label='ilość kabli')
    core = forms.IntegerField(label='ilość żył na fazę')
    layer_factor = forms.DecimalField(max_digits=3, decimal_places=2, min_value=0.1, max_value=1, label='współczynnik ułożenia')
    overload_factor = forms.ChoiceField(choices=overload_factor_choices, label='współczynnik wyzwalania')
    length = forms.IntegerField(label='długość', help_text='[m]')

    class Meta:
        model = Cable
        fields = ('material', 'insulation', 'cable_cross_section', 'cable_routing',)
        labels = {
            'material': 'materiał',
            'insulation': 'izolacja',
            'cable_cross_section': 'przekrój',
            'cable_routing': 'sposób ułożenia',
        }

        help_texts = {
            'cable_cross_section': '[m2]',

        }

class ProtectionDevicesResultForm(forms.ModelForm):

    off_time = forms.DecimalField(max_digits=2, decimal_places=1, min_value=0.2, max_value=5, label='czas wyłączenia')

    class Meta:
        model = ProtectionDevices
        fields = ('type', 'current',)
        labels = {
            'type': 'typ',
            'current': 'prąd',
        }

        help_texts = {
            'current': '[A]',
        }

class ResultsForm(forms.Form):
    Ib_current = forms.FloatField(label='prąd szczytowy obwodu', help_text='[A]')
    In_current = forms.FloatField(label='prąd nastawy zabezpieczenia', help_text='[A]')
    Idd_current = forms.FloatField(label='obciążalność długotrwała', help_text='[A]')
    voltage_drop = forms.FloatField(label='spadek napięcia', help_text='[%]')


class OverloadConditionsForm(forms.Form):
    Idd_current_condition = forms.CharField(label='Idd > Ib', disabled=True)
    overload_current_condition = forms.CharField(label='I2 > 1,45xIb', disabled=True)
