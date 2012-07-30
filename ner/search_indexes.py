'''
This file has been created for the django-haystack installation
'''

import datetime
from haystack.indexes import *
from haystack import site 
from ner.models import Person, Requirement, FTCQualification, Vacancy, Certificate, Organisation, ShipExperience, Compensation


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

class CompensationIndex(SearchIndex):
    text = CharField(document=True,use_template=True)
    date_of_claim = DateField(model_attr='date_of_claim')
    date_accident_reported = DateField(model_attr='date_accident_reported')
    date_of_accident = DateField(model_attr='date_of_accident')
    injured_person = CharField(model_attr='injured_person')

    def get_model(self):
        return Compensation

site.register(Person, PersonIndex)
site.register(Vacancy, VacancyIndex)
site.register(Compensation, CompensationIndex)
site.register(Organisation, OrganisationIndex)
