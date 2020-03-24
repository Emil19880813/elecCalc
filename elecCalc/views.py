# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import View
from django.shortcuts import render, redirect


# Create your views here.
from elecCalc.forms import ReceiverForm, CableForm, ProtectionDevicesForm, ResultsForm, OverloadConditionsForm, \
     GroupReceiverForm, CircuitForm
from elecCalc.models import Cable, ProtectionDevices, Receiver, GroupReceiver


class MainPage(View):
    def get(self, request):
        receiver_form = ReceiverForm()
        circuit_form = CircuitForm()
        cable_form = CableForm()
        devices_form = ProtectionDevicesForm()
        results_form = ResultsForm()
        overload_form = OverloadConditionsForm()
        return render(request, 'main_page.html', context={'receiver_form': receiver_form, 'circuit_form': circuit_form,
                                                          'cable_form': cable_form, 'devices_form': devices_form,
                                                          'results_form': results_form, 'overload_form': overload_form})

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

class DisplayGroupReceiverView(View):
    def get(self, request):
        group_receivers = GroupReceiver.objects.all()
        return render(request, 'display_group_receiver.html', context={'group_receivers': group_receivers})

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

class EditGroupReceiverView(View):
    def get(self, request, group_id):
        group = GroupReceiver.objects.get(pk=group_id)
        group_form = GroupReceiverForm(instance=group)
        return render(request, "edit_group.html", context={"form": group_form})
    def post(self, request, group_id):
        group = GroupReceiver.objects.get(pk=group_id)
        group_form = GroupReceiverForm(request.POST, instance=group)
        if group_form.is_valid():
            group_form.save()
            return redirect('elecCalc:display-group-receiver')

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

class DeleteGroupReceiverView(View):
    def get(self, request, group_id):
        GroupReceiver.objects.get(pk=group_id).delete()
        return redirect('elecCalc:display-group-receiver')

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

class AddGroupReceiverView(View):
    def get(self, request):
        group_form = GroupReceiverForm()
        return render(request, "add_group_receiver.html", context={"form": group_form})
    def post(self, request):
        group_form = GroupReceiverForm(request.POST)
        if group_form.is_valid():
            #dodać walidację "brak możliwości dublowania wpisów"
            group_form.save()
        return redirect('elecCalc:display-group-receiver')

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