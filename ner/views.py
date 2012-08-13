from ner.models import Vacancy, Person, Certificate, Compensation, Organisation
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    vacancy_list = Vacancy.open.all()
    return render_to_response('ner/index.html', {'vacancy_list': vacancy_list})

@login_required
def search(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    return render_to_response('ner/search.html', request)
