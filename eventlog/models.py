# -*- coding: utf-8 -*-

from django.db import models

from eventlog.fields import JSONField

class Event(models.Model):
    CLASS_TYPE = (
        ('L', 'EVENT'),
        ('D', 'DEBUG'),
        ('W', 'WARNING'),
        ('E', 'ERROR'),
    )
    name = models.CharField(max_length=50)
    evt_class = models.CharField(u'Event Class',
                                 max_length=2,
                                 choices=CLASS_TYPE,
                                 default='L')
    filename = models.CharField(u'Filename', max_length=100)
    function = models.CharField(u'Function', max_length=25)
    line = models.CharField(u'Line Number', max_length=7)
    timestamp = models.DateTimeField(u'Timestamp',
                                     auto_now_add = True)
    data = JSONField(blank=True)

    def __unicode__(self):
        return "%s:%s %s" % (self.evt_class, self.name, self.timestamp)
