from django.shortcuts import render
from django.views import View
from resume.models import Resume


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resumes.html', context={'resumes': Resume.objects.all()})
