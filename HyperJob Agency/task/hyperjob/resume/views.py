from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden
from resume.models import Resume


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resumes.html', context={'resumes': Resume.objects.all()})

class ResumeNewView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/new.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            return HttpResponseForbidden()
        description = request.POST.get('description')
        Resume.objects.create(description=description,
                              author=request.user,
                              )
        return redirect('/home')
