# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django import forms


# Create your views here.
from elecCalc.forms import CableForm, ProtectionDevicesForm, CableSelectForm
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

        CalculationResult.objects.create(cir_number=circuit_number, cir_name=receiver_name, cir_voltage=voltage, cir_power=power, cir_cos_fi=power_factor, cir_current=i_b,
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


class CableListView(View):
    def get(self, request):
        results = CalculationResult.objects.all()
        return render(request, 'cable_list.html', context={'results': results})

class CableIddView(View):
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
class DisplayCableView(View):
    def get(self, request):
        cables = Cable.objects.all()
        return render(request, 'display_cable.html', context={'cables': cables})

class DisplayDevicesView(View):
    def get(self, request):
        devices = ProtectionDevices.objects.all()
        return render(request, 'display_device.html', context={'devices': devices})

class DisplayReceiverView(View):
    def get(self, request):
        receivers = Receiver.objects.all()
        return render(request, 'display_receiver.html', context={'receivers': receivers})


#TODO: edit data
class EditCableView(View):
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

class EditDeviceView(View):
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


class EditReceiverView(View):
    def get(self, request, receiver_id):
        receiver = Receiver.objects.get(pk=receiver_id)
        receiver_form = ReceiverForm(instance=receiver)
        return render(request, "edit_receiver.html", context={"form": receiver_form})
    def post(self, request, receiver_id):
        receiver = Receiver.objects.get(pk=receiver_id)
        receiver_form = ReceiverForm(request.POST, instance=receiver)
        if receiver_form.is_valid():
            receiver_form.save()
            return redirect('elecCalc:display-receiver')

#TODO: remove data
class DeleteCableView(View):
    def get(self, request, cable_id):
        Cable.objects.get(pk=cable_id).delete()
        return redirect('elecCalc:display-cable')

class DeleteDeviceView(View):
    def get(self, request, device_id):
        ProtectionDevices.objects.get(pk=device_id).delete()
        return redirect('elecCalc:display-device')


class DeleteReceiverView(View):
    def get(self, request, receiver_id):
        Receiver.objects.get(pk=receiver_id).delete()
        return redirect('elecCalc:display-receiver')


#TODO: add data
class AddCableView(View):
    def get(self, request):
        cable_form = CableForm()
        return render(request, "add_cable.html", context={"form": cable_form})
    def post(self, request):
        cable_form = CableForm(request.POST)
        if cable_form.is_valid():
            #dodać walidację "brak możliwości dublowania wpisów"
            cable_form.save()
        return redirect('elecCalc:display-cable')

class AddDeviceView(View):
    def get(self, request):
        device_form = ProtectionDevicesForm()
        return render(request, "add_device.html", context={"form": device_form})
    def post(self, request):
        device_form = ProtectionDevicesForm(request.POST)
        if device_form.is_valid():
            #dodać walidację "brak możliwości dublowania wpisów"
            device_form.save()
        return redirect('elecCalc:display-device')


class AddReceiverView(View):
    def get(self, request):
        receiver_form = ReceiverForm()
        return render(request, "add_group_receiver.html", context={"form": receiver_form})
    def post(self, request):
        receiver_form = ReceiverForm(request.POST)
        if receiver_form.is_valid():
            #dodać walidację "brak możliwości dublowania wpisów"
            receiver_form.save()
        return redirect('elecCalc:display-receiver')

'''

'''