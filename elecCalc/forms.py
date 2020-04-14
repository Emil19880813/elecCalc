from crispy_forms.bootstrap import PrependedAppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from elecCalc.models import Cable, ProtectionDevices


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

class ProtectionDevicesForm(forms.ModelForm):
    class Meta:
        model = ProtectionDevices
        fields = '__all__'
        help_texts = {
            'name': 'nazwa',
            'type': 'typ',
            'current': 'prąd',
        }

class CableSelectForm(forms.ModelForm):
    class Meta:
        model = Cable
        exclude = ['capacity']
        help_texts = {
            'material': 'materiał',
            'insulation': 'izolacja',
            'cable_cross_section': 'przekrój',
            'cable_routing': 'sposób ułożenia',
        }

    def __init__(self, *args, **kwargs):
        super(CableSelectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('material', css_class='form-group col-md-1 mb-0'),
                Column('insulation', css_class='form-group col-md-1 mb-0'),
                Column('cable_cross_section', css_class='form-group col-md-1 mb-0'),
                Column('cable_routing', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            return username
        except ObjectDoesNotExist:
            raise forms.ValidationError('Niepoprawna nazwa użytkownika')

    def clean_password(self):
        if 'username' in self.cleaned_data:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                return password
            raise forms.ValidationError('Niepoprawne hasło')


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')

    def clean_password2(self):
        ps = self.cleaned_data
        if ps['password2'] != ps['password']:
            raise forms.ValidationError('Hasła nie są identyczne.')
        return ps['password2']

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


