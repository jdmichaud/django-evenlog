# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'eventlog_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('evt_class', self.gf('django.db.models.fields.CharField')(default='L', max_length=2)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('timestamp', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('data', self.gf('eventlog.fields.JSONCharField')(max_length=255)),
        ))
        db.send_create_signal(u'eventlog', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'eventlog_event')


    models = {
        u'eventlog.event': {
            'Meta': {'object_name': 'Event'},
            'data': ('eventlog.fields.JSONCharField', [], {'max_length': '255'}),
            'evt_class': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '2'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['eventlog']