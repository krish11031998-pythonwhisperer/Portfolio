from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.person)
admin.site.register(models.work_exp)
admin.site.register(models.Project)
admin.site.register(models.Skill)
admin.site.register(models.Description)
admin.site.register(models.Tech_Framework)

