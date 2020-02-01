from django.shortcuts import render
from .models import work_exp,Project,Description,person

# Create your views here.

def index(request):
	return render(request,'p_app/index.html',context={'Person': person.objects.all(),'w_exp':work_exp.objects.all(),'projects':Project.objects.all()[:4],'projects_2':Project.objects.all()[4:],'description':Description.objects.all()})