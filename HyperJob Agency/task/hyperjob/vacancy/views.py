from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden
from vacancy.models import Vacancy

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancies.html', context={'vacancies': Vacancy.objects.all()})

class VacancyNewView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancies.html')

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden()
        description = request.POST.get('description')
        Vacancy.objects.create(description=description,
                               author=request.user,
                               )
        return redirect('/home')