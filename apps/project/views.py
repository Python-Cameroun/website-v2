from django.shortcuts import render, get_object_or_404
from .models import Project


def projects_view(request):
    projects = Project.objects.all()
    return render (request, 'project/projects.html', {'projects':projects})

def project_view(request,slug):
    project = get_object_or_404(Project,slug = slug)
    return render (request, 'project/project.html', {'project':project})
