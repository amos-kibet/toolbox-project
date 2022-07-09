from django.shortcuts import render
from toolbox.models import Project

# Create your views here.
def index(request):
  projects = Project.objects.all()
  context = {
    'projects': projects
  }

  return render(request, 'index.html', context)

def read_more(request, pk):
  project = Project.objects.get(pk=pk)
  context = {
    'project': project
  }
  
  return render(request, 'read_more.html', context)
