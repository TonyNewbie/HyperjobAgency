from django.shortcuts import render
from django.views import View
from .models import Resume


# Create your views here.
class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resumes.html', context={'resumes': resumes})


