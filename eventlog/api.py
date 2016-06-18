# -*- coding: utf-8 -*-
import inspect
from eventlog.models import Event


# Extract from the DB the Event corresponding
# to the parameters. Kwargs is a dict matching the
# data in the data field
def filter_event(name=None, evt_class=None, **kwargs):
    pass


# Log an event into the DB
def log_event(name, evt_class='E', **kwargs):
    (frame, filename, line,
     function, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    Event(name=name,
          evt_class=evt_class,
          filename=filename,
          function=function,
          line=line,
          data=kwargs).save()
