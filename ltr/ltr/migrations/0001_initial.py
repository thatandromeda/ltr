# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Questionnaire'
        db.create_table(u'ltr_questionnaire', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q1', self.gf('django.db.models.fields.TextField')()),
            ('q2', self.gf('django.db.models.fields.TextField')()),
            ('q3', self.gf('django.db.models.fields.TextField')()),
            ('q4', self.gf('django.db.models.fields.TextField')()),
            ('q5', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ltr', ['Questionnaire'])

        # Adding model 'Person'
        db.create_table(u'ltr_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('library_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('contacted_on', self.gf('django.db.models.fields.DateField')()),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person', to=orm['ltr.Questionnaire'])),
        ))
        db.send_create_signal(u'ltr', ['Person'])

        # Adding model 'Script'
        db.create_table(u'ltr_script', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('problem_solved', self.gf('django.db.models.fields.TextField')()),
            ('impact', self.gf('django.db.models.fields.TextField')()),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('permission', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permission_notes', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(related_name='script', to=orm['ltr.Questionnaire'])),
        ))
        db.send_create_signal(u'ltr', ['Script'])


    def backwards(self, orm):
        # Deleting model 'Questionnaire'
        db.delete_table(u'ltr_questionnaire')

        # Deleting model 'Person'
        db.delete_table(u'ltr_person')

        # Deleting model 'Script'
        db.delete_table(u'ltr_script')


    models = {
        u'ltr.person': {
            'Meta': {'object_name': 'Person'},
            'contacted_on': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'library_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person'", 'to': u"orm['ltr.Questionnaire']"}),
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
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'script'", 'to': u"orm['ltr.Questionnaire']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ltr']