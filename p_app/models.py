from django.db import models

# Create your models here.

class person(models.Model):
	img = models.ImageField(upload_to='images/')
	Name = models.CharField(max_length =150)
	dob = models.CharField(max_length=150)
	email = models.CharField(max_length=75,blank=True,null=True)
	linkedin = models.CharField(max_length= 100)
	github = models.CharField(max_length= 100)


	def __str__(self):
		return self.Name

class work_exp(models.Model):
	designation = models.CharField(max_length=150)
	year = models.CharField(max_length=150)
	location = models.CharField(max_length=75,blank=True,null=True)
	company = models.CharField(max_length=50,null=True)
	P_1 = models.CharField(max_length= 500)
	P_2 = models.CharField(max_length= 500)
	P_3 = models.CharField(max_length= 500)

	def __str__(self):
		return self.designation


class Skill(models.Model):

	skill = models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.skill

class Tech_Framework(models.Model):
    
	tech = models.CharField(max_length=50)
	frameworks = models.ManyToManyField(Skill)

	def __str__(self):
		return self.tech

class Project(models.Model):

	tag = models.CharField('Add the tag for this project',max_length=100,blank=True)
	headline = models.CharField('Name of the project',max_length=100,blank=True)
	img_url = models.ImageField(upload_to='images/')
	skill = models.ManyToManyField(Skill)

	def __str__(self):
		return self.headline


class Description(models.Model):

	tag = models.CharField(max_length=200,null=True)
	description = models.CharField(max_length=500,null=True)
	project = models.ForeignKey(Project,on_delete=models.CASCADE)

	def __str__(self):
		return self.tag


class Skill_pb(models.Model):

	name = models.CharField(max_length=50,blank=False)
	value_percent = models.IntegerField(blank=False)
	tag = models.CharField(max_length=50,null=True,blank=False)
	icon_tag = models.CharField(max_length=20,null=True,blank=True)

	def __str__(self):
		return self.name
