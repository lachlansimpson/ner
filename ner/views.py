from ner.models import Vacancy
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required


from django.views.generic import DetailView
from ner.models import Person, Compensation, Organisation, Vacancy, Certificate


class PersonDetailView(DetailView):
    context_object_name = "person"
    model = Person

    def get_context_data(self,**kwargs):
        #Call the base implementation first to get a context
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        #Add in a queryset of all the Vacancies
        context['job_list'] = Vacancy.objects.all()
        context['certificate_list'] = Certificate.objects.all()
        context['claim_list'] = Compensation.objects.all()
        return context

class OrganisationDetailView(DetailView):
    context_object_name = "organisation"
    model = Organisation

    def get_context_data(self,**kwargs):
        #Call the base implementation first to get a context
        context = super(OrganisationDetailView, self).get_context_data(**kwargs)
        #Add in a queryset of all the Vacancies
        context['job_list'] = Vacancy.objects.all()
        context['claim_list'] = Compensation.objects.all()
        return context


@login_required
def index(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    vacancy_list = Vacancy.open.all()
    return render_to_response('ner/index.html', {'vacancy_list': vacancy_list})
