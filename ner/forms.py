"""
makes the objects available via the admin interface
"""
from ner.models import Person, Organisation, Experience, FTCQualification, Certificate, Vacancy, Requirement, ShipExperience
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.contrib import admin
from django.forms import ModelForm
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget 
import datetime
from django.forms.models import modelformset_factory

this_year = datetime.date.today().year
YEARS_LIST = range(this_year-51, this_year-16)

class CertInline(admin.TabularInline):
    model = Certificate
    template = 'admin/collapsed_tabular_inline.html'

#class CertificateForm(ModelForm):
 #   model = Certificate

#CertFormset = modelformset_factory(CertificateForm)

class FTCQualInline(admin.TabularInline):
    model = FTCQualification
    extra = 1
    template = 'admin/collapsed_tabular_inline.html'

class ExperienceInline(admin.TabularInline):
    model = Experience
    template = 'admin/collapsed_tabular_inline.html'

class ShipXPInline(admin.TabularInline):
    model = ShipExperience
    template = 'admin/collapsed_tabular_inline.html'

class PersonForm(ModelForm):
    class Meta:
        model = Person 
        #this_year = datetime.date.today().year
        #years_list = range(this_year-51, this_year-16)
        '''
        TODO fix this damn years problem: currently have made the adjustment in 
        ~/src/envs/mlhrd/lib/python2.7/site-packages/django/forms/extras/widgets.py
        '''
        #years = range(1999-2012)
        widgets = {
            #'dob': SelectDateWidget(YEARS_LIST),
            'dob': SelectDateWidget(),
            'gender': RadioSelect(),
        }

#    formset = CertFormset()

    fieldsets = [
         ('Biographical', {'fields':[('first_name', 'surname'), 'dob', 'gender']}),
         ('Contact Information', {'fields':['email', 'phone_mobile', 'phone_home', 'phone_other'], 'classes':['collapse']}),
         ('Address and Island Information', {'fields':['current_address', 'previous_address', 'birth_place', 'home_island',
                                                       'island_represented'],'classes':['collapse']}),
         ('Other Information', {'fields':['marital_status',
                                         'number_of_dependants', 'religion',
                                         'passport_no', 'discharge_book',
                                         'medical_test_date'],'classes':['collapse']}),

         ]
    inlines = [CertInline, ExperienceInline, ShipXPInline, FTCQualInline]

class OrganisationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields':[('name', 'island'), 'address']}),
        ('Contact details',
         {'fields':[('contact_name','contact_email'),('contact_phone_1','contact_phone_2')],
          'classes':['collapse']}),
        ('extra', {'fields':[('category','industry')], 'classes':['collapse']}), 
    ]
