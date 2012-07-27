from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from ner.models import Person, Organisation, Vacancy, Requirement, Compensation
from ner.admin import PersonAdmin, CertInline, ExperienceInline, ShipXPInline, FTCQualInline
import datetime
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('ner.views',
        url(r'^$', 'index'),

        url(r'^people/all/$',
            ListView.as_view(queryset=Person.people.all().order_by('surname'),
                             template_name="ner/all_person_list.html")),

        url(r'^people/$', ListView.as_view(queryset=Person.workers.all())),
        
        url(r'^person/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Person), name='person_view'),

        url(r'^person/add/$',
            CreateView.as_view(
                template_name='ner/person_create.html',
                form_class=PersonAdmin)),

        url(r'^person/(?P<pk>\d+)/edit/$',
            UpdateView.as_view(
                model=Person)),
        
        url(r'^orgs/$',
            ListView.as_view(
                queryset=Organisation.objects.all().order_by('name'),
                template_name="ner/org_list.html")),
        
        url(r'^orgs/islands/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/org_island_list.html")),
        
        url(r'^orgs/isic/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/org_isic_list.html")),
        
        url(r'^orgs/category/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/org_cat_list.html")),
        
        url(r'^organisation/(?P<slug>[-\w]+)/$',
            DetailView.as_view(
                model=Organisation,
                template_name='ner/organisation_detail.html'),
                name='organisation_view'),

        url(r'^vacancies/requirements/$',
            ListView.as_view(
                queryset=Requirement.objects.all().order_by("req_name"),
                template_name="ner/vac_req_list.html")),
        
        url(r'^vacancies/recent/$',
            ListView.as_view(
                queryset=Vacancy.recent.all(),
                template_name="ner/recent_vacancy_list.html")),
        
        url(r'^vacancies/$',
            ListView.as_view(
                queryset=Vacancy.open.all())),
        
        url(r'^vacancies/all/$',
            ListView.as_view(
                queryset=Vacancy.complete.all())),
        
        url(r'^vacancy/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
            DetailView.as_view(
                model=Vacancy),
            name='vacancy_view'),
        
        url(r'^compensation/all/$',
            ListView.as_view(queryset=Compensation.objects.all().order_by('date_of_claim'),
                             template_name="ner/all_compensation_list.html")),
)

urlpatterns += staticfiles_urlpatterns()
