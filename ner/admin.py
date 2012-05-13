"""
makes the objects available via the admin interface
"""
from ner.models import Person, Organisation, Experience, FTCQualification, Certificate, Vacancy, Requirement, ShipExperience
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.contrib import admin
from django.forms import ModelForm, ValidationError
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget 
import datetime

class CertInline(admin.TabularInline):
    model = Certificate
    template = 'admin/collapsed_tabular_inline.html'

class FTCQualInline(admin.TabularInline):
    model = FTCQualification
    extra = 1
    template = 'admin/collapsed_tabular_inline.html'

class XPAdminForm(ModelForm):
    class Meta:
        model = Experience
        widgets = {
            'start_date': SelectDateWidget(),
            'end_date': SelectDateWidget(),
        }
    
    def clean(self):
        cleaned_data = super(XPAdminForm, self).clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")

        if end < start:
             raise ValidationError("Experience end date is before it's start date")

        return cleaned_data

class ExperienceInline(admin.TabularInline):
    model = Experience
    template = 'admin/collapsed_tabular_inline.html'
    form = XPAdminForm

class ShipXPInline(admin.TabularInline):
    model = ShipExperience
    template = 'admin/collapsed_tabular_inline.html'

class PersonAdminForm(ModelForm):
    class Meta:
        model = Person 
        this_year = datetime.date.today().year
        YEARS_LIST = range(this_year-51, this_year-16)
        widgets = {
            'dob': SelectDateWidget(years=YEARS_LIST),
            'gender': RadioSelect(),
            'medical_test_date': SelectDateWidget(),
        }

class PersonAdmin(admin.ModelAdmin):
    filter_horizontal = ("skills",)
    fieldsets = [
        ('Biographical', {'fields':[('first_name', 'surname'), 
                                    ('dob', 'gender')]}),
        ('Contact Information', {'fields':[('email', 'phone_mobile'), 
                                           ('phone_home', 'phone_other')],
                                            'classes':['collapse']}),
        ('Address and Island Information', {'fields':['current_address', 'previous_address', 
                                                      ('birth_place',
                                                       'home_island',
                                                       'island_represented')],
                                                       'classes':['collapse']}),
        ('Other Information', {'fields':[('marital_status', 'number_of_dependants'), 
                                         'religion',
                                         ('passport_no', 'discharge_book'),
                                         'medical_test_date'],
                                         'classes':['collapse']}),
        ('Skills', {'fields':['skills'],'classes':['collapse']}),
    ]
    inlines = [CertInline, ExperienceInline, ShipXPInline, FTCQualInline]
    list_filter = ('gender',)
    list_display = ('first_name','surname','birth_place',)
    search_fields = ('first_name',)#'surname','dob','email',)
    form = PersonAdminForm

class OrganisationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields':[('name', 'island'), 'address']}),
        ('Contact details',
         {'fields':[('contact_name','contact_email'),('contact_phone_1','contact_phone_2')],
          'classes':['collapse']}),
        ('extra', {'fields':[('category','industry')], 'classes':['collapse']}), 
    ]

class VacancyAdmin(admin.ModelAdmin):
    filter_horizontal = ("requirements","certificates")
    fieldsets = [
        ('Basic Details',
         {'fields':[('title','closing_date'),'organisation','division'],
          'classes':['collapse']}),
        ('Salary details',
         {'fields':[('salary_level_1','salary_level_2'),('salary_level_3','salary_level_4')],
          'classes':['collapse']}),
        ('Requirements',
         {'fields':['certificates','requirements'],
          'classes':['collapse']}),
    ]
    list_filter = ('closing_date',)
    
admin.site.register(Person, PersonAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Requirement)
