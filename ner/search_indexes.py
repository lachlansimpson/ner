'''
This file has been created for the django-haystack installation
'''

import datetime
from haystack.indexes import *
from haystack import site 
from ner.models import Person, Requirement, FTCQualification, Vacancy, Certificate, Organisation, ShipExperience


class PersonIndex(SearchIndex):
	text = CharField(document=True, use_template=True)
	surname = CharField(model_attr='surname')
	first_name = CharField(model_attr='first_name')
	
	def get_model(self):
		return Person


site.register(Person, PersonIndex)
