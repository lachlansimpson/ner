"""
makes the objects available via the admin interface
"""
from ner.models import * 
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.contrib import admin
from django.forms import ModelForm, ValidationError
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget 
import datetime

this_year = datetime.date.today().year
BIRTH_YEARS = range(this_year-51, this_year-16)
XP_YEARS = range(this_year-25,this_year+1)

class ApplicantsInline(admin.StackedInline):
    model = Vacancy.applicants.through
    verbose_name='Has applied for'
    verbose_name_plural='Jobs Applied For'

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
            'start_date': SelectDateWidget(years=XP_YEARS),
            'end_date': SelectDateWidget(years=XP_YEARS),
        }
    
    def clean(self):
        cleaned_data = super(XPAdminForm, self).clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")

        if end < start:
             raise ValidationError("Experience end date is before it's start date")
        elif end == start:
             raise ValidationError("Experience end date is the same day as it's start date")
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
        widgets = {
            'dob': SelectDateWidget(years=BIRTH_YEARS),
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
    inlines = [CertInline, ExperienceInline, ShipXPInline, FTCQualInline, ApplicantsInline]
    list_filter = ('gender',)
    list_display = ('first_name','surname','birth_place',)
    search_fields = ('first_name',)
    form = PersonAdminForm

class OrganisationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        ('', {'fields':[('name', 'island'), 'address']}),
        ('Contact details',
         {'fields':[('contact_name','contact_email'),('contact_phone_1','contact_phone_2')],
          'classes':['collapse']}),
        ('extra', {'fields':[('category','industry'), 'slug'], 'classes':['collapse']}), 
    ]

class VacancyAdminForm(ModelForm):
    class Meta:
        model = Vacancy
    
    def clean(self):
        cleaned_data = super(VacancyAdminForm, self).clean()
        salary_1 = cleaned_data.get('salary_level_1')
        salary_2 = cleaned_data.get('salary_level_2')
        salary_3 = cleaned_data.get('salary_level_3')
        salary_4 = cleaned_data.get('salary_level_4')

        '''
        The salary ranges go from high (salary_1) to low (salary_4)
        If there are any NA, they need to start at salary_4 and work back to
        salary_1 
        A vacancy must have at least one salary level
        '''
        if not ((salary_1 > salary_2 > salary_3 > salary_4) or
            (salary_1 > salary_2 > salary_3 and salary_4 == 'NA') or
            (salary_1 > salary_2 and salary_3 == salary_4 == 'NA') or
            (salary_1 != 'NA' and salary_2 == salary_3 == salary_4 == 'NA') or
            (salary_1 == salary_2 == salary_3 == salary_4 == 'NA')):
             raise ValidationError("Salary ranges need to start at a high and progressively go to a lower level. ")
        return cleaned_data

class VacancyAdmin(admin.ModelAdmin):
    filter_horizontal = ("requirements",)
    fieldsets = [
        ('Basic Details',
         {'fields':[('title','closing_date'),'organisation','division'],
          'classes':['collapse']}),
        ('Salary details',
         {'fields':[('salary_level_1','salary_level_2'),('salary_level_3','salary_level_4')],
          'classes':['collapse']}),
        ('Requirements',
         {'fields':['requirements'],
          'classes':['collapse']}),
        ('Applicants',
         {'fields':['applicants'],
          'classes':['collapse']}),
    ]
    list_filter = ('closing_date',)
    form = VacancyAdminForm

admin.site.register(Person, PersonAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Requirement)
