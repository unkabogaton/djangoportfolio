from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def index(request):
    template='index.html'
    projects= Project.objects.all()
    context={'projects': projects}
    return render(request, template, context)

def proj_detail(request, proj_id):
    template='proj_detail.html'
    project=get_object_or_404(Project, pk=proj_id)
    context={'project':project}
    return render(request, template, context)
