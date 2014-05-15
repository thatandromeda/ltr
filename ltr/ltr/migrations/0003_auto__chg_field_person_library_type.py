# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Person.library_type'
        db.alter_column(u'ltr_person', 'library_type', self.gf('django.db.models.fields.CharField')(max_length=3))

    def backwards(self, orm):

        # Changing field 'Person.library_type'
        db.alter_column(u'ltr_person', 'library_type', self.gf('django.db.models.fields.CharField')(max_length=2))

    models = {
        u'ltr.person': {
            'Meta': {'object_name': 'Person'},
            'contacted_on': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'library_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person'", 'null': 'True', 'to': u"orm['ltr.Questionnaire']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ltr.questionnaire': {
            'Meta': {'object_name': 'Questionnaire'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q1': ('django.db.models.fields.TextField', [], {}),
            'q2': ('django.db.models.fields.TextField', [], {}),
            'q3': ('django.db.models.fields.TextField', [], {}),
            'q4': ('django.db.models.fields.TextField', [], {}),
            'q5': ('django.db.models.fields.TextField', [], {})
        },
        u'ltr.script': {
            'Meta': {'object_name': 'Script'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.TextField', [], {}),
            'permission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'problem_solved': ('django.db.models.fields.TextField', [], {}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'script'", 'null': 'True', 'to': u"orm['ltr.Questionnaire']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ltr']