# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event.timestamp'
        db.alter_column(u'eventlog_event', 'timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Event.timestamp'
        db.alter_column(u'eventlog_event', 'timestamp', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'eventlog.event': {
            'Meta': {'object_name': 'Event'},
            'data': ('eventlog.fields.JSONCharField', [], {'max_length': '255', 'blank': 'True'}),
            'evt_class': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '2'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['eventlog']