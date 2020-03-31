# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from elecCalc.models import Receiver, Cable, ProtectionDevices

admin.site.register(Receiver)
admin.site.register(Cable)
admin.site.register(ProtectionDevices)
