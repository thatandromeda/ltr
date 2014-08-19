# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.contacted_on'
        db.delete_column(u'ltr_person', 'contacted_on')


        # Changing field 'Questionnaire.q1'
        db.alter_column(u'ltr_questionnaire', 'q1', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Person.contacted_on'
        raise RuntimeError("Cannot reverse this migration. 'Person.contacted_on' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Person.contacted_on'
        db.add_column(u'ltr_person', 'contacted_on',
                      self.gf('django.db.models.fields.DateField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Questionnaire.q1'
        raise RuntimeError("Cannot reverse this migration. 'Questionnaire.q1' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Questionnaire.q1'
        db.alter_column(u'ltr_questionnaire', 'q1', self.gf('django.db.models.fields.TextField')())

    models = {
        u'ltr.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'library_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person'", 'null': 'True', 'to': u"orm['ltr.Questionnaire']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ltr.questionnaire': {
            'Meta': {'ordering': "['name']", 'object_name': 'Questionnaire'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'q1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q2': ('django.db.models.fields.TextField', [], {}),
            'q3': ('django.db.models.fields.TextField', [], {}),
            'q4': ('django.db.models.fields.TextField', [], {}),
            'q5': ('django.db.models.fields.TextField', [], {}),
            'q6': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ltr.script': {
            'Meta': {'object_name': 'Script'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'permission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'problem_solved': ('django.db.models.fields.TextField', [], {}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'script'", 'null': 'True', 'to': u"orm['ltr.Questionnaire']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ltr']