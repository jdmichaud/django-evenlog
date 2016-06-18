# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django import forms
from django.forms import ModelForm, ValidationError
from django.forms.models import BaseInlineFormSet

from eventlog.models import Event

class ClassListFilter(SimpleListFilter):
    title = 'Class filter'
    parameter_name = 'evt_class'

    def lookups(self, request, model_admin):
        return Event.CLASS_TYPE

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset.all()
        else:
            return queryset.filter(evt_class = self.value())

class NameListFilter(SimpleListFilter):
    title = 'Name filter'
    parameter_name = 'name'

    def lookups(self, request, model_admin):
        names = [name[0] for name in Event.objects.values_list('name').distinct()]
        names = zip(names, names)
        return names

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset.all()
        else:
            return queryset.filter(name = self.value())

class EventAdmin(admin.ModelAdmin):
    list_filter = (ClassListFilter, NameListFilter)
    list_display = ('id', 'evt_class', 'name', 'timestamp', 'data')
    search_fields = [ 'name', 'data' ]
