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

class OrganisationIndex(SearchIndex):
    text = CharField(document=True,use_template=True)
    name = CharField(model_attr='name')

    def get_model(self):
        return Organisation

class VacancyIndex(SearchIndex):
    text = CharField(document=True,use_template=True)
    title = CharField(model_attr='title')
    closing_date = DateField(model_attr='closing_date')
    organisation = CharField(model_attr='organisation')

    def get_model(self):
        return Vacancy

site.register(Person, PersonIndex)
site.register(Vacancy, VacancyIndex)
site.register(Organisation, OrganisationIndex)
