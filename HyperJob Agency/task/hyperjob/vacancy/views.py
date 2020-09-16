from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancies.html', context={'vacancies': Vacancy.objects.all()})