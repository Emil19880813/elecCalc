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
            return HttpResponse('ok')

            '''
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            name = cable_selection_form.cleaned_data.get('name')
            

            

            i_r = devices.current * devices.kr_factor
            i_dd = Cable.objects.filter(material=cable.material, insulation=cable.insulation,
                                        cable_cross_section=cable.cable_cross_section,
                                        cable_routing=cable.cable_routing).first().capacity
            i_2 = devices.off_time * i_dd
            if receiver.voltage == '0.23':
                i_b = receiver.power * 1000 / (receiver.power_factor * receiver.voltage * 1000)
                delta_u = 2 * receiver.power * 1000 * cable.length * 100 / (
                            56 * cable.cable_cross_section * pow(receiver.voltage * 1000, 2))
                return render(request, 'main_page.html',
                              context={'i_r': i_r, 'i_dd': i_dd, 'i_2': i_2, 'i_b': i_b, 'delta_u': delta_u})
            i_b = receiver.power * 1000 / (math.sqrt(3) * receiver.power_factor * receiver.voltage * 1000)
            delta_u = receiver.power * 1000 * cable.length * 100 / (
                        56 * cable.cable_cross_section * pow(receiver.voltage * 1000, 2))
            return render(request, 'main_page.html',
                          context={'i_r': i_r, 'i_dd': i_dd, 'i_2': i_2, 'i_b': i_b, 'delta_u': delta_u})
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