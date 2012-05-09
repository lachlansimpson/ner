# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('ner_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length='1')),
            ('marital_status', self.gf('django.db.models.fields.CharField')(default='S', max_length=1, blank='True')),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=15, blank='True')),
            ('number_of_dependants', self.gf('django.db.models.fields.IntegerField')(null='True', blank='True')),
            ('current_address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('previous_address', self.gf('django.db.models.fields.CharField')(max_length=60, blank='True')),
            ('home_island', self.gf('django.db.models.fields.CharField')(default='01', max_length=2, blank='True')),
            ('birth_place', self.gf('django.db.models.fields.CharField')(default='01', max_length=2, blank='True')),
            ('island_represented', self.gf('django.db.models.fields.CharField')(default='01', max_length=2, blank='True')),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=12, blank='True')),
            ('phone_home', self.gf('django.db.models.fields.CharField')(max_length=8, blank='True')),
            ('phone_other', self.gf('django.db.models.fields.CharField')(max_length=12, blank='True')),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank='True')),
            ('passport_no', self.gf('django.db.models.fields.CharField')(max_length=6, blank='True')),
            ('discharge_book', self.gf('django.db.models.fields.CharField')(max_length=12, blank='True')),
            ('medical_test_date', self.gf('django.db.models.fields.DateField')(null='True', blank='True')),
        ))
        db.send_create_signal('ner', ['Person'])

        # Adding model 'FTCQualification'
        db.create_table('ner_ftcqualification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ner.Person'], null='True', blank='True')),
            ('cadet_no', self.gf('django.db.models.fields.CharField')(max_length=12, blank='True')),
            ('year_grad', self.gf('django.db.models.fields.CharField')(max_length=5, blank='True')),
        ))
        db.send_create_signal('ner', ['FTCQualification'])

        # Adding model 'Certificate'
        db.create_table('ner_certificate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ner.Person'], null='True', blank='True')),
            ('institute', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('course_content', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('ner', ['Certificate'])

        # Adding model 'Organisation'
        db.create_table('ner_organisation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('island', self.gf('django.db.models.fields.CharField')(max_length=2, blank='True')),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=40, blank='True')),
            ('contact_phone_1', self.gf('django.db.models.fields.CharField')(max_length=9, blank='True')),
            ('contact_phone_2', self.gf('django.db.models.fields.CharField')(max_length=9, blank='True')),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=4, blank='True')),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('ner', ['Organisation'])

        # Adding model 'Requirement'
        db.create_table('ner_requirement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('req_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('req_notes', self.gf('django.db.models.fields.CharField')(max_length=100, blank='True')),
        ))
        db.send_create_signal('ner', ['Requirement'])

        # Adding model 'Vacancy'
        db.create_table('ner_vacancy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('occupation_code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ner.Organisation'])),
            ('division', self.gf('django.db.models.fields.CharField')(max_length=30, blank='True')),
            ('salary_level_1', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('salary_level_2', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('salary_level_3', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('salary_level_4', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('closing_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('ner', ['Vacancy'])

        # Adding M2M table for field requirements on 'Vacancy'
        db.create_table('ner_vacancy_requirements', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vacancy', models.ForeignKey(orm['ner.vacancy'], null=False)),
            ('requirement', models.ForeignKey(orm['ner.requirement'], null=False))
        ))
        db.create_unique('ner_vacancy_requirements', ['vacancy_id', 'requirement_id'])

        # Adding model 'Experience'
        db.create_table('ner_experience', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ner.Person'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ner.Organisation'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('reference_name', self.gf('django.db.models.fields.CharField')(max_length=30, null='True', blank='True')),
            ('reference_contact_email', self.gf('django.db.models.fields.CharField')(max_length=40, null='True', blank='True')),
            ('reference_contact_phone', self.gf('django.db.models.fields.CharField')(max_length=10, null='True', blank='True')),
        ))
        db.send_create_signal('ner', ['Experience'])

        # Adding model 'ShipExperience'
        db.create_table('ner_shipexperience', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ner.Person'], null='True', blank='True')),
            ('recruiting_agency', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('embark_date', self.gf('django.db.models.fields.DateField')()),
            ('disembark_date', self.gf('django.db.models.fields.DateField')()),
            ('vessel_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('vessel_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('vessel_company', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('ner', ['ShipExperience'])

    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('ner_person')

        # Deleting model 'FTCQualification'
        db.delete_table('ner_ftcqualification')

        # Deleting model 'Certificate'
        db.delete_table('ner_certificate')

        # Deleting model 'Organisation'
        db.delete_table('ner_organisation')

        # Deleting model 'Requirement'
        db.delete_table('ner_requirement')

        # Deleting model 'Vacancy'
        db.delete_table('ner_vacancy')

        # Removing M2M table for field requirements on 'Vacancy'
        db.delete_table('ner_vacancy_requirements')

        # Deleting model 'Experience'
        db.delete_table('ner_experience')

        # Deleting model 'ShipExperience'
        db.delete_table('ner_shipexperience')

    models = {
        'ner.certificate': {
            'Meta': {'object_name': 'Certificate'},
            'course_content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Person']", 'null': "'True'", 'blank': "'True'"}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ner.experience': {
            'Meta': {'object_name': 'Experience'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Person']"}),
            'reference_contact_email': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': "'True'", 'blank': "'True'"}),
            'reference_contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': "'True'", 'blank': "'True'"}),
            'reference_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': "'True'", 'blank': "'True'"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'ner.ftcqualification': {
            'Meta': {'object_name': 'FTCQualification'},
            'cadet_no': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Person']", 'null': "'True'", 'blank': "'True'"}),
            'year_grad': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': "'True'"})
        },
        'ner.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': "'True'"}),
            'contact_phone_1': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': "'True'"}),
            'contact_phone_2': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': "'True'"}),
            'island': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': "'True'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'ner.person': {
            'Meta': {'object_name': 'Person'},
            'birth_place': ('django.db.models.fields.CharField', [], {'default': "'01'", 'max_length': '2', 'blank': "'True'"}),
            'current_address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'discharge_book': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': "'True'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': "'1'"}),
            'home_island': ('django.db.models.fields.CharField', [], {'default': "'01'", 'max_length': '2', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'island_represented': ('django.db.models.fields.CharField', [], {'default': "'01'", 'max_length': '2', 'blank': "'True'"}),
            'marital_status': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1', 'blank': "'True'"}),
            'medical_test_date': ('django.db.models.fields.DateField', [], {'null': "'True'", 'blank': "'True'"}),
            'number_of_dependants': ('django.db.models.fields.IntegerField', [], {'null': "'True'", 'blank': "'True'"}),
            'passport_no': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': "'True'"}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': "'True'"}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'phone_other': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'previous_address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': "'True'"}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': "'True'"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ner.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'req_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'req_notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'True'"})
        },
        'ner.shipexperience': {
            'Meta': {'object_name': 'ShipExperience'},
            'disembark_date': ('django.db.models.fields.DateField', [], {}),
            'embark_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Person']", 'null': "'True'", 'blank': "'True'"}),
            'recruiting_agency': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'vessel_company': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'vessel_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vessel_type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ner.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            'closing_date': ('django.db.models.fields.DateField', [], {}),
            'division': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Organisation']"}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ner.Requirement']", 'symmetrical': 'False'}),
            'salary_level_1': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'salary_level_2': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'salary_level_3': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'salary_level_4': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ner']