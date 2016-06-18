# -*- coding: utf-8 -*-

from django.contrib import admin

from eventlog.models import Event
from eventlog.admin.event_admin  import EventAdmin

admin.site.register(Event, EventAdmin)
