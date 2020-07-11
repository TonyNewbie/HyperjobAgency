from django.shortcuts import render
from django.views import View
from .models import Vacancy


# Create your views here.
class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancies.html', context={'vacancies': vacancies})
