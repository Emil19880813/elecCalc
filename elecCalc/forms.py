
from crispy_forms.bootstrap import PrependedAppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms

from elecCalc.models import Receiver, Cable, ProtectionDevices


class CableSelectionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CableSelectionForm, self).__init__(*args, **kwargs)
        self.fields['circuit_number'] = forms.CharField(max_length=12, help_text='numer obwodu')

        self.fields['material'] = forms.ChoiceField(help_text='materiał',
            choices=((cable.material, cable.get_material_display()) for cable in Cable.objects.all().distinct('material')))
        self.fields['insulation'] = forms.ChoiceField(help_text='izolacja',
            choices=((cable.insulation, cable.get_insulation_display) for cable in Cable.objects.all().distinct('insulation')))
        self.fields['cable_cross_section'] = forms.ChoiceField(help_text='przekrój',
            choices=((cable.cable_cross_section, cable.get_cable_cross_section_display) for cable in Cable.objects.all().distinct('cable_cross_section')))
        self.fields['cable_routing'] = forms.ChoiceField(help_text='sposób ułożenia',
            choices=((cable.cable_routing, cable.get_cable_routing_display) for cable in Cable.objects.all().distinct('cable_routing')))
        self.fields['amount'] = forms.IntegerField(max_value=8, min_value=1, help_text='ilość kabli',)
        self.fields['core'] = forms.IntegerField(max_value=8, min_value=1, help_text='ilość żył na fazę',)
        self.fields['layer_factor'] = forms.DecimalField(max_digits=3, decimal_places=2, max_value=1, min_value=0.1, help_text='współczynnik ułożenia',)
        self.fields['length'] = forms.IntegerField(max_value=250, min_value=1, help_text='długość',)

        self.fields['type'] = forms.ChoiceField(help_text='typ',
            choices=((device.type, device.get_type_display) for device in ProtectionDevices.objects.all().distinct('type')))
        self.fields['current'] = forms.ChoiceField(help_text='prąd znamionowy',
            choices=((device.current, device.get_current_display) for device in ProtectionDevices.objects.all().distinct('current')))
        self.fields['kr_factor'] = forms.DecimalField(max_digits=3, decimal_places=2, max_value=1, min_value=0.1, help_text='nastawa członu przeciążeniowego',)
        self.fields['off_time'] = forms.ChoiceField(choices=((0, 0.2), (1, 0.4), (2, 5)), help_text='czas wyłączenia')
        self.fields['k2_factor'] = forms.ChoiceField(choices=((0, 1.2), (1, 1.45), (2, 1.6), (3, 1.9)), help_text='współczynnik k2')


        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('circuit_number', css_class='form-group col-md-2 mb-0'),
                Column('name', css_class='form-group col-md-2 mb-0'),
                Column(PrependedAppendedText('voltage','Uo=','kV', css_class='form-group col-md-4 mb-0')),
                Column(PrependedAppendedText('power','Po','kW', css_class='form-group col-md-4 mb-0')),
                Column(PrependedText('power_factor', 'cos fi=', css_class='form-group col-md-4 mb-0')),
                css_class='form-row'
            ),
            Row(
                Column('material', css_class='form-group col-md-1 mb-0'),
                Column('insulation', css_class='form-group col-md-1 mb-0'),
                Column(PrependedAppendedText('cable_cross_section', 'S=', 'mm2', css_class='form-group col-md-4 mb-0')),
                Column('cable_routing', css_class='form-group col-md-1 mb-0'),
                Column('amount', css_class='form-group col-md-1 mb-0'),
                Column('core',  css_class='form-group col-md-1 mb-0'),
                Column(PrependedText('layer_factor', 'kc', css_class='form-group col-md-4 mb-0')),
                Column(PrependedAppendedText('length', 'l=', 'mb', css_class='form-group col-md-4 mb-0')),
                css_class='form-row'
            ),
            Row(
                Column('type', css_class='form-group col-md-1 mb-0'),
                Column(PrependedAppendedText('current','Ib', 'A', css_class='form-group col-md-4 mb-0')),
                Column(PrependedText('kr_factor', 'kr', css_class='form-group col-md-4 mb-0')),
                Column(PrependedAppendedText('off_time', 't', 's',  css_class='form-group col-md-4 mb-0')),
                Column(PrependedText('k2_factor', 'k2',  css_class='form-group col-md-4 mb-0')),
                css_class='form-row'
            ),
        )

    class Meta:
        model = Receiver
        fields = '__all__'
        help_texts = {
            'name': 'nazwa',
            'voltage': 'napięcie',
            'power': 'moc czynna',
            'power_factor': 'współczynnik mocy',
        }


class CableForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = '__all__'
        help_texts = {
            'material': 'materiał',
            'insulation': 'izolacja',
            'cable_cross_section': 'przekrój',
            'capacity': 'obciążaloność długotrwała',
            'cable_routing': 'sposób ułożenia',
        }

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = '__all__'
        help_texts = {
            'name': 'nazwa/typ',
            'voltage': 'napięcie znamionowe',
            'power': 'moc czynna',
            'power_factor': 'współczynnik mocy',
        }


class ProtectionDevicesForm(forms.ModelForm):
    class Meta:
        model = ProtectionDevices
        fields = '__all__'
        help_texts = {
            'name': 'nazwa',
            'type': 'typ',
            'current': 'prąd',
        }

class ResultsForm(forms.Form):
    Ib_current = forms.FloatField(label='prąd szczytowy obwodu', help_text='[A]')
    In_current = forms.FloatField(label='prąd nastawy zabezpieczenia', help_text='[A]')
    Idd_current = forms.FloatField(label='obciążalność długotrwała', help_text='[A]')
    voltage_drop = forms.FloatField(label='spadek napięcia', help_text='[%]')
