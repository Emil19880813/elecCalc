
from crispy_forms.bootstrap import PrependedAppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms
from elecCalc.models import Receiver, GroupReceiver, Cable, ProtectionDevices


class ReceiverForm(forms.ModelForm):

    class Meta:
        model = Receiver
        exclude = ['group']
        labels = {
            'circuit_number': 'numer obwodu',
            'name': 'nazwa',
            'voltage': 'napięcie',
            'power': 'moc',
            'power_factor': 'współczynnik mocy',
        }

    def __init__(self, *args, **kwargs):
        super(ReceiverForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('circuit_number', css_class='form-group col-md-2 mb-0'),
                Column('name', css_class='form-group col-md-2 mb-0'),
                Column(PrependedAppendedText('voltage','Uo=','kV', css_class='form-group col-md-4 mb-0')),
                Column(PrependedAppendedText('power','Po','kW', css_class='form-group col-md-4 mb-0')),
                Column(PrependedText('power_factor', 'cos fi=', css_class='form-group col-md-4 mb-0')),
                css_class='form-row'
            ),
        )

class GroupReceiverForm(forms.ModelForm):
    class Meta:
        model = GroupReceiver
        fields = '__all__'


class CableForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = '__all__'
        labels = {
            'material': 'materiał',
            'insulation': 'izolacja',
            'cable_cross_section': 'przekrój',
            'cable_routing': 'sposób ułożenia',
            'amount': 'ilość kabli',
            'core': 'ilość żył/faza',
            'layer_factor': 'współczynik ułożenia',
            'overload_factor': 'współczynnik przeciążenia',
            'length': 'długość',
        }

    def __init__(self, *args, **kwargs):
        super(CableForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('material', css_class='form-group col-md-1 mb-0'),
                Column('insulation', css_class='form-group col-md-1 mb-0'),
                Column(PrependedAppendedText('cable_cross_section','Uo=','kV', css_class='form-group col-md-1 mb-0')),
                Column('cable_routing', css_class='form-group col-md-1 mb-0'),
                Column('amount', css_class='form-group col-md-1 mb-0'),
                Column('core', css_class='form-group col-md-1 mb-0'),
                Column('layer_factor', css_class='form-group col-md-1 mb-0'),
                Column('overload_factor', css_class='form-group col-md-1 mb-0'),
                Column(PrependedAppendedText('length','Po','kW', css_class='form-group col-md-1 mb-0')),
                css_class='form-row'
            ),
        )

class ProtectionDevicesForm(forms.ModelForm):
    class Meta:
        model = ProtectionDevices
        fields = '__all__'
        labels = {
            'type': 'typ',
            'current': 'prąd',
            'off_time': 'czas wyłączenia',
        }

    def __init__(self, *args, **kwargs):
        super(ProtectionDevicesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('type', css_class='form-group col-md-3 mb-0'),
                Column(PrependedAppendedText('current','Uo=','kV', css_class='form-group col-md-6 mb-0')),
                Column(PrependedAppendedText('off_time','Uo=','kV', css_class='form-group col-md-6 mb-0')),
                css_class='form-row'
            ),
        )

class ResultsForm(forms.Form):
    Ib_current = forms.FloatField(label='prąd szczytowy obwodu', help_text='[A]')
    In_current = forms.FloatField(label='prąd nastawy zabezpieczenia', help_text='[A]')
    Idd_current = forms.FloatField(label='obciążalność długotrwała', help_text='[A]')
    voltage_drop = forms.FloatField(label='spadek napięcia', help_text='[%]')


class OverloadConditionsForm(forms.Form):
    Idd_current_condition = forms.CharField(label='Idd > Ib', disabled=True)
    overload_current_condition = forms.CharField(label='I2 > 1,45xIb', disabled=True)


'''
    self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'

        self.helper.layout = Layout(
            Div(
                Div('group', css_class="col-md-2 mt-4"),
                Div('circuit_number', css_class="col-md-2 mt-4"),
                Div('name', css_class="col-md-2 mt-4"),
                Div(PrependedAppendedText('voltage','%', '%', css_class="col-md-6 mt-0")),
                Div(PrependedAppendedText('power','%', '%', css_class="col-md-5 mt-0")),
                Div(PrependedText('power_factor','%', css_class="col-md-5 mt-0")),
                css_class='row',
'''