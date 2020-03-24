from django import forms
from elecCalc.models import Receiver, GroupReceiver, Cable, ProtectionDevices, Circuit


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        exclude = ['circuit_number']
        labels = {
            'name': 'nazwa',
        }

class GroupReceiverForm(forms.ModelForm):
    class Meta:
        model = GroupReceiver
        fields = '__all__'


class CircuitForm(forms.ModelForm):
    class Meta:
        model = Circuit
        fields = '__all__'
        labels = {
                    'number': 'numer obwodu',
        }

class CableForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = '__all__'
        labels = {
            'material': 'materiał',
        }

class ProtectionDevicesForm(forms.ModelForm):
    class Meta:
        model = ProtectionDevices
        fields = '__all__'
        labels = {
            'name': 'nazwa',
        }

class ResultsForm(forms.Form):
    Ib_current = forms.FloatField(label='prąd szczytowy obwodu', help_text='[A]')
    In_current = forms.FloatField(label='prąd nastawy zabezpieczenia', help_text='[A]')
    Idd_current = forms.FloatField(label='obciążalność długotrwała', help_text='[A]')
    voltage_drop = forms.FloatField(label='spadek napięcia', help_text='[%]')


class OverloadConditionsForm(forms.Form):
    Idd_current_condition = forms.CharField(label='Idd > Ib', disabled=True)
    overload_current_condition = forms.CharField(label='I2 > 1,45xIb', disabled=True)
