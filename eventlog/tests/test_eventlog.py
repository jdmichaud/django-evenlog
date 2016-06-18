# -*- coding: utf-8 -*-

import re
import json
import inspect
import logging

from django.test import TestCase

from eventlog.utils import EventFactory

from eventlog.models import Event
from eventlog.api import log_event
from eventlog.api import filter_event

class EventLogTest(TestCase):
    def setUp(self):
        pass

    # Function not yet implemented
    def _test_filter(self):
        EventFactory(name='some_name',
                     evt_class='L',
                     data={ 'fieldA' : 1, 'fieldB' : 'qwe' })
        EventFactory(name='some_other_name',
                     evt_class='W',
                     data={ 'fieldA' : 2, 'fieldB' : 'qwe' })
        EventFactory(name='some_name',
                     evt_class='E',
                     data={ 'fieldA' : 1 })
        EventFactory(name='some_other_name',
                     evt_class='E',
                     data={ 'fieldA' : 1, 'fieldB' : 'ewq' })
        self.assertEqual(2, len(filter_event(name = 'some_name')))
        self.assertEqual(2, len(filter_event(name = 'some_other_name')))
        self.assertEqual(2, len(filter_event(evt_class = 'E')))
        self.assertEqual(1, len(filter_event(evt_class = 'W')))
        self.assertEqual(3, len(filter_event(kwargs = { 'fieldA' : 1 })))
        self.assertEqual(3, len(filter_event(kwargs = { 'fieldA' : 1, 'fieldB' : 'ewq' })))

    def test_log_event_default(self):
        log_event('some_name')
        self.assertEqual(1, len(Event.objects.all()))
        log_event('some_other_name')
        self.assertEqual(2, len(Event.objects.all()))
        log_event('some_other_name')
        self.assertEqual(3, len(Event.objects.all()))
        # Check event content
        self.assertEqual('some_name', Event.objects.get(pk=1).name)
        self.assertEqual('some_other_name', Event.objects.get(pk=2).name)
        self.assertEqual('some_other_name', Event.objects.get(pk=3).name)
        # test default value
        self.assertEqual('E', Event.objects.get(pk=3).evt_class)

    def test_log_event_with_evt_class(self):
        for (index, (eclass, descr)) in enumerate(Event.CLASS_TYPE):
            log_event('some_name', evt_class=eclass)
            self.assertEqual(eclass, Event.objects.get(pk=index+1).evt_class)

    def test_log_event_with_kwargs(self):
        log_event('some_name', evt_class = 'E', fieldA = 1, fieldB = ['a', 'b'])
        e = Event.objects.all()[0]
        self.assertTrue('fieldA' in e.data)
        self.assertTrue('fieldB' in e.data)
        # Check evt_class does not appear in the JSONField        
        self.assertTrue('evt_class' not in e.data)        

    def test_log_event_frame_data(self):
        (filename, line, function, lines, index) = inspect.getframeinfo(inspect.currentframe())
        log_event('some_name')
        # test frame data
        self.assertEqual(filename, Event.objects.get(pk=1).filename)
        self.assertEqual(function, Event.objects.get(pk=1).function)
        self.assertEqual(str(line + 1), Event.objects.get(pk=1).line)

    # Function not yet implemented
    def _test_log_event_web_api(self):
        self.assertTrue(False)
