from django.shortcuts import render
from .models import work_exp,Project,Description,person,Tech_Framework

# Create your views here.

def index(request):
	return render(request,'p_app/index.html',context={'Person': person.objects.all(),'w_exp':work_exp.objects.all(),'tech_frameworks':Tech_Framework.objects.all(),'projects':Project.objects.all()[:4],'projects_2':Project.objects.all()[4:],'description':Description.objects.all()})