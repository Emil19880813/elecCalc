# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math, csv

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpRequest

# Create your views here.
from elecCalc.forms import CableForm, ProtectionDevicesForm, CableSelectForm, LoginForm, RegisterForm
from elecCalc.models import Cable, ProtectionDevices, CalculationResult


class Choices:

    voltage_choices = (
        (0, 0.23),
        (1, 0.4),
        (2, 15),
    )

    time_off = (
        (0, 0.2),
        (1, 0.4),
        (2, 5),
    )

    k2_factor = (
        (0, 1.2),
        (1, 1.45),
        (2, 1.6),
        (3, 1.9),
    )

class MainPage(View):

    def get(self, request):

        voltages = [voltage[1] for voltage in Choices.voltage_choices]
        materials = [cable for cable in Cable.objects.all().distinct('material')]
        insulations = [cable for cable in Cable.objects.all().distinct('insulation')]
        cable_cross_sections = [cable for cable in Cable.objects.all().distinct('cable_cross_section')]
        cables_routing = [cable for cable in Cable.objects.all().distinct('cable_routing')]
        names = [devices for devices in ProtectionDevices.objects.all().distinct('name')]
        currents = [devices for devices in ProtectionDevices.objects.all().distinct('current')]
        times_off = [time_off[1] for time_off in Choices.time_off]
        k2_factors = [k2_factor[1] for k2_factor in Choices.k2_factor]
        return render(request, 'main_page.html', context={'voltages': voltages, 'materials': materials,
                                                          'insulations': insulations, 'cable_cross_sections': cable_cross_sections,
                                                          'cables_routing': cables_routing, 'names': names, 'currents': currents,
                                                          'times_off': times_off, 'k2_factors': k2_factors})

    def post(self, request):
        position = int(CalculationResult.objects.all().count()) + 1
        voltages = [voltage[1] for voltage in Choices.voltage_choices]
        materials = [cable for cable in Cable.objects.all().distinct('material')]
        insulations = [cable for cable in Cable.objects.all().distinct('insulation')]
        cable_cross_sections = [cable for cable in Cable.objects.all().distinct('cable_cross_section')]
        cables_routing = [cable for cable in Cable.objects.all().distinct('cable_routing')]
        names = [devices for devices in ProtectionDevices.objects.all().distinct('name')]
        currents = [devices for devices in ProtectionDevices.objects.all().distinct('current')]
        times_off = [time_off[1] for time_off in Choices.time_off]
        k2_factors = [k2_factor[1] for k2_factor in Choices.k2_factor]

        circuit_number = request.POST.get('circuit_number')
        receiver_name = request.POST.get('receiver_name')
        voltage = float(request.POST.get('voltage'))
        power = int(request.POST.get('power'))
        power_factor = float(request.POST.get('power_factor'))
        material = request.POST.get('material')
        insulation = request.POST.get('insulation')
        cable_cross_section = request.POST.get('cable_cross_section')
        cable_routing = request.POST.get('cable_routing')
        amount = int(request.POST.get('amount'))
        core = int(request.POST.get('core'))
        layer_factor = float(request.POST.get('layer_factor'))
        length = int(request.POST.get('length'))
        device_type = request.POST.get('device_type')
        current = int(request.POST.get('current'))
        kr_factor = float(request.POST.get('kr_factor'))
        off_time = float(request.POST.get('off_time'))
        k2_factor = float(request.POST.get('k2_factor'))
        i_dd = float(Cable.objects.filter(material=material, insulation=insulation,
                                      cable_cross_section=cable_cross_section,
                                      cable_routing=cable_routing).first().capacity)
        i_z = round(i_dd * layer_factor, 2)# obciązalność długotrwała
        i_r = round(current * kr_factor, 2) # prąd nastawy zabezpieczenia przeciążeniowego
        i_2 = round(i_r * k2_factor, 2)
        second_condition = bool(1.45 * i_z >= i_2)

        if voltage == 0.23:
            i_b = round(power * 1000 / (power_factor * voltage * 1000), 2) # prąd szczytowy obwodu
            delta_u = round(2 * power * 1000 * length * 100 / (
                    56 * float(cable_cross_section) * pow(voltage * 1000, 2)), 2)
            first_condition = bool(i_z >= i_r >= i_b)
        else:
            i_b = round(power * 1000 / (math.sqrt(3) * power_factor * voltage * 1000), 2)
            delta_u = round(2 * power * 1000 * length * 100 / (
                    56 * float(cable_cross_section) * pow(voltage * 1000, 2)), 2)
            first_condition = bool(i_z >= i_r >= i_b)

        CalculationResult.objects.create(position=position, cir_number=circuit_number, cir_name=receiver_name, cir_voltage=voltage, cir_power=power, cir_cos_fi=power_factor, cir_current=i_b,
                                                  cab_amount=amount, core_amount=core, cab_routing=cable_routing, cab_insulation=insulation, cab_material=material,
                                                  cab_cable_cross_section=float(cable_cross_section), cab_length=length, cab_i_dd=i_dd, cab_kc_factor=layer_factor,
                                                  cab_i_z=i_z, dev_type=device_type, dev_current=current, dev_kr_factor=kr_factor, dev_i_r=i_r,
                                                  dev_k2_factor=k2_factor, dev_i_2=i_2, conditions=str(first_condition), cab_vol_drop=delta_u)

        return render(request, 'main_page.html', context={'voltages': voltages, 'materials': materials,
                                                      'insulations': insulations,
                                                      'cable_cross_sections': cable_cross_sections,
                                                      'cables_routing': cables_routing, 'names': names,
                                                      'currents': currents,
                                                      'times_off': times_off, 'k2_factors': k2_factors,
                                                      'i_r': i_r, 'i_z': i_z, 'i_2': i_2, 'i_b': i_b,
                                                      'delta_u': delta_u, 'first_condition': first_condition,
                                                      'second_condition': second_condition})


class CableListView(LoginRequiredMixin, View):
    def get(self, request):
        results = CalculationResult.objects.all().order_by('position')
        return render(request, 'cable_list.html', context={'results': results})


class PositionChange(LoginRequiredMixin, View):
    def post(self, request):
        pos_nr = request.POST.get('pos_nr')
        if pos_nr:
            result = CalculationResult.objects.get(position=int(pos_nr))
            if CalculationResult.objects.filter(position=(int(pos_nr) + 1)).exists():
                next_result = CalculationResult.objects.get(position=(int(pos_nr) + 1))
                result.position = int(result.position)
                next_result.position = int(next_result.position)
                result.position += 1
                result.save()
                next_result.position -= 1
                next_result.save()
                return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'bad'})

class CableIddView(LoginRequiredMixin, View):
    def get(self, request):
        cables = Cable.objects.all()
        cable_select_form = CableSelectForm()
        return render(request, 'display_idd.html', context={'cables': cables, 'cable_select_form': cable_select_form})
    def post(self, request):
        cables = Cable.objects.all()
        cable_select_form = CableSelectForm(request.POST)
        if cable_select_form.is_valid():
            material = cable_select_form.cleaned_data.get('material')
            insulation = cable_select_form.cleaned_data.get('insulation')
            cable_cross_section = cable_select_form.cleaned_data.get('cable_cross_section')
            cable_routing = cable_select_form.cleaned_data.get('cable_routing')

            result = Cable.objects.filter(material=material, insulation=insulation,
                                          cable_cross_section=cable_cross_section, cable_routing=cable_routing)[0]
            return render(request, 'display_idd.html', context={'cables': cables, 'cable_select_form': cable_select_form, 'result': result})


#TODO: wyświetlanie danych
class DisplayCableView(LoginRequiredMixin, View):
    def get(self, request):
        cables = Cable.objects.all()
        return render(request, 'display_cable.html', context={'cables': cables})


class DisplayDevicesView(View):
    def get(self, request):
        devices = ProtectionDevices.objects.all()
        return render(request, 'display_device.html', context={'devices': devices})


#TODO: edit data
class EditCableView(LoginRequiredMixin, View):
    def get(self, request, cable_id):
        cable = Cable.objects.get(pk=cable_id)
        cable_form = CableForm(instance=cable)
        return render(request, "edit_cable.html", context={"form": cable_form})
    def post(self, request, cable_id):
        cable = Cable.objects.get(pk=cable_id)
        cable_form = CableForm(request.POST, instance=cable)
        if cable_form.is_valid():
            cable_form.save()
            return redirect('elecCalc:display-cable')


class EditDeviceView(LoginRequiredMixin, View):
    def get(self, request, device_id):
        device = ProtectionDevices.objects.get(pk=device_id)
        device_form = ProtectionDevicesForm(instance=device)
        return render(request, "edit_device.html", context={"form": device_form})
    def post(self, request, device_id):
        device = ProtectionDevices.objects.get(pk=device_id)
        device_form = ProtectionDevicesForm(request.POST, instance=device)
        if device_form.is_valid():
            device_form.save()
            return redirect('elecCalc:display-device')


#TODO: remove data
class DeleteCableView(LoginRequiredMixin, View):
    def get(self, request, cable_id):
        Cable.objects.get(pk=cable_id).delete()
        return redirect('elecCalc:display-cable')


class DeleteDeviceView(LoginRequiredMixin, View):
    def get(self, request, device_id):
        ProtectionDevices.objects.get(pk=device_id).delete()
        return redirect('elecCalc:display-device')


class DeleteResultView(LoginRequiredMixin, View):
    def get(self, request, result_id):
        CalculationResult.objects.get(pk=result_id).delete()
        return redirect('elecCalc:cable-list')


#TODO: add data
class AddCableView(LoginRequiredMixin, View):
    def get(self, request):
        cable_form = CableForm()
        return render(request, "add_cable.html", context={"form": cable_form})
    def post(self, request):
        cable_form = CableForm(request.POST)
        if cable_form.is_valid():
            #dodać walidację "brak możliwości dublowania wpisów"
            cable_form.save()
        return redirect('elecCalc:display-cable')


class AddDeviceView(LoginRequiredMixin, View):
    def get(self, request):
        device_form = ProtectionDevicesForm()
        return render(request, "add_device.html", context={"form": device_form})
    def post(self, request):
        device_form = ProtectionDevicesForm(request.POST)
        if device_form.is_valid():
            #dodać walidację "brak możliwości dublowania wpisów"
            device_form.save()
        return redirect('elecCalc:display-device')


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, "account/login.html", context={"form": login_form})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('elecCalc:main_page')
                else:
                    return HttpResponse('Konto jest zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane logowania')
        return render(request, "account/login.html", context={"form": login_form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('elecCalc:login')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', context={'form': form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            return render(request, 'account/register_done.html', context={'new_user': new_user})
        return render(request, 'account/register.html', context={'form': form})

@login_required
def export_to_csv(request):
    mod = CalculationResult._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(mod.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in mod.get_fields()]
    writer.writerow([field.verbose_name for field in fields])
    for obj in CalculationResult.objects.all():
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            data_row.append(value)
        writer.writerow(data_row)
    return response

