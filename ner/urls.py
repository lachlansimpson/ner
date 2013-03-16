from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from ner.models import Person, Organisation, Vacancy, Requirement, Compensation
from ner.admin import PersonAdmin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('ner.views',
        url(r'^$', 'index'),
        url(r'^search/$', 'search'),
        
        url(r'^people/$', ListView.as_view(queryset=Person.workers.all())),
        
        url(r'^people/all/$',
            ListView.as_view(queryset=Person.people.all().order_by('surname'),
                             template_name="ner/person_all.html")),

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
                template_name="ner/organisation_all.html")),
        
        url(r'^orgs/islands/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/organisation_island_list.html")),
        
        url(r'^orgs/isic/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/organisation_isic_list.html")),
        
        url(r'^orgs/category/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/organisation_category_list.html")),
        
        url(r'^organisation/(?P<slug>[-\w]+)/$',
            DetailView.as_view(
                model=Organisation,
                template_name='ner/organisation_detail.html'),
                name='organisation_view'),

        url(r'^vacancies/requirements/$',
            ListView.as_view(
                queryset=Requirement.objects.all().order_by("req_name"),
                template_name="ner/vacancy_requirements_list.html")),
        
        url(r'^vacancies/recent/$',
            ListView.as_view(
                queryset=Vacancy.recent.all(),
                template_name="ner/vacancy_recent_list.html")),
        
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
        
        url(r'^compensation/paid/$',
            ListView.as_view(queryset=Compensation.paid.all(),
                             template_name="ner/compensation_paid.html")),
        
        url(r'^compensation/rejected/$',
            ListView.as_view(queryset=Compensation.rejected.all(),
                             template_name="ner/compensation_rejected.html")),
        
        url(r'^compensation/pending/$',
            ListView.as_view(queryset=Compensation.pending.all(),
                             template_name="ner/compensation_pending.html")),
        
        url(r'^compensation/processing/$',
            ListView.as_view(queryset=Compensation.processing.all(),
                             template_name="ner/compensation_processing.html")),
        
        url(r'^compensation/all/$',
            ListView.as_view(queryset=Compensation.complete.all().order_by('date_of_claim'),
                             template_name="ner/compensation_all.html")),
        
        url(r'^compensation/$',
            ListView.as_view(queryset=Compensation.current.all().order_by('date_of_claim'),
                             template_name="ner/compensation_current.html")),
        
        url(r'^compensation/(?P<slug>[-\w]+)/$',
            DetailView.as_view(
                model=Compensation,
                template_name='ner/compensation_detail.html'),
                name='compensation_claim_view'),
)

urlpatterns += staticfiles_urlpatterns()
