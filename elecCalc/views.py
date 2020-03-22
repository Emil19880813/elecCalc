# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from elecCalc.forms import ReceiverForm, CableForm, ProtectionDevicesForm, ResultsForm, OverloadConditionsForm, \
    ReceiverResultForm, CableResultForm, ProtectionDevicesResultForm
from elecCalc.models import Cable, ProtectionDevices, Receiver, GroupReceiver


class MainPage(View):
    def get(self, request):
        receiver_form = ReceiverResultForm()
        cable_form = CableResultForm()
        devices_form = ProtectionDevicesResultForm()
        results_form = ResultsForm()
        overload_form = OverloadConditionsForm()
        return render(request, 'main_page.html', context={'receiver_form': receiver_form, 'cable_form': cable_form,
                                                          'devices_form': devices_form, 'results_form': results_form,
                                                          'overload_form': overload_form,
                                                          })
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

#TODO: edytowanie danych
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