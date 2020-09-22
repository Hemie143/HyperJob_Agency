from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/main.html')


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                # return render(request, 'vacancy/new.html')
                return redirect('/vacancy/new')
            else:
                # return render(request, 'resume/new.html')
                return redirect('/resume/new')
        else:
            return render(request, 'hyperjob/login.html')

    def post(self, request):
        pass
