"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from hyperjob.views import MainPageView, MyLoginView, MySignupView, HomeView
from vacancy.views import VacanciesView, VacancyNewView
from resume.views import ResumesView, ResumeNewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancy/new', VacancyNewView.as_view()),
    path('resumes/', ResumesView.as_view()),
    path('resume/new', ResumeNewView.as_view()),
    path('login', MyLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup', MySignupView.as_view()),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('home', HomeView.as_view()),
    path('', MainPageView.as_view()),
]


'''
1. Make a "templates" directory (store future HTML files) in hyperjob
2. In templates make an HTML file with the required info
3. Create a views.py file in hyperjob
4. Add the path in the urls.py file
'''