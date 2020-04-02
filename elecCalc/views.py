# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect


# Create your views here.
from elecCalc.forms import CableForm, ProtectionDevicesForm, CableSelectionForm, ReceiverForm
from elecCalc.models import Cable, ProtectionDevices, Receiver


class MainPage(View):
    def get(self, request):
        cable_selection_form = CableSelectionForm()
        return render(request, 'main_page.html', context={'cable_selection_form': cable_selection_form})

    def post(self, request):
        cable_selection_form = CableSelectionForm(request.POST)
        if cable_selection_form.is_valid():
            circuit_number = cable_selection_form.cleaned_data.get('circuit_number')
            name = cable_selection_form.cleaned_data.get('name')
            voltage = cable_selection_form.cleaned_data.get('voltage')
            power = cable_selection_form.cleaned_data.get('power')
            power_factor = cable_selection_form.cleaned_data.get('power_factor')
            material = cable_selection_form.cleaned_data.get('material')
            insulation = cable_selection_form.cleaned_data.get('insulation')
            cable_cross_section = cable_selection_form.cleaned_data.get('cable_cross_section')
            cable_routing = cable_selection_form.cleaned_data.get('cable_routing')
            amount = cable_selection_form.cleaned_data.get('amount')
            core = cable_selection_form.cleaned_data.get('core')
            layer_factor = cable_selection_form.cleaned_data.get('layer_factor')
            length = cable_selection_form.cleaned_data.get('length')
            type = cable_selection_form.cleaned_data.get('current')
            current = cable_selection_form.cleaned_data.get('current')
            kr_factor = cable_selection_form.cleaned_data.get('kr_factor')
            off_time = cable_selection_form.cleaned_data.get('off_time')
            k2_factor = cable_selection_form.cleaned_data.get('k2_factor')
            return HttpResponse('działa')
'''
            #i_r = current * kr_factor
            i_dd = float(Cable.objects.filter(material=material, insulation=insulation,
                                        cable_cross_section=cable_cross_section,
                                        cable_routing=cable_routing).first().capacity)


            return render(request, 'main_page.html',
                          context={'cable_selection_form': cable_selection_form, 'i_dd': i_dd})

            i_2 = off_time * i_dd
            if voltage == '0.23':
                i_b = power * 1000 / (power_factor * voltage * 1000)
                delta_u = 2 * power * 1000 * length * 100 / (
                            56 * cable_cross_section * pow(voltage * 1000, 2))
                return render(request, 'main_page.html',
                              context={'cable_selection_form': cable_selection_form, 'i_r': i_r, 'i_dd': i_dd,
                                       'i_2': i_2, 'i_b': i_b, 'delta_u': delta_u})
            i_b = power * 1000 / (math.sqrt(3) * power_factor * voltage * 1000)
            delta_u = power * 1000 * length * 100 / (
                        56 * cable_cross_section * pow(voltage * 1000, 2))
            return render(request, 'main_page.html',
                          context={'cable_selection_form': cable_selection_form, 'i_r': i_r, 'i_dd': i_dd, 'i_2': i_2,
                                   'i_b': i_b, 'delta_u': delta_u})
'''

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