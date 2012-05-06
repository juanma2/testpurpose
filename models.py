from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
##Include Extends for user class

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#extra fields	
	extra_field = models.CharField(max_length = 100, blank=True)

def create_user_profile (sender,instance,created, **kwargs):
	if created:
		User.Profile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)

class PrimaryElementMTM(models.Model):
	name_mtm = models.CharField(max_length=25)
	extra_info_mtm = models.CharField(max_length = 100,blank=True)

class SonOfPrimaryMTM(models.Model):
	name_son_mtm = models.CharField(max_length=25)
	irrelevant_info_mtm = models.CharField(max_length = 100, blank= True)
	myfather_MTM = models.ManyToManyField(PrimaryElementMTM)


class PrimaryElementOPK(models.Model):
	name_opk = models.CharField(max_length=25)
	extra_info_opk = models.CharField(max_length = 100,blank=True)

class SonOfPrimaryOPK(models.Model):
	name_son_opk = models.CharField(max_length=25)
	irrelevant_info_opk = models.CharField(max_length = 100, blank= True)
	myfather_opk = models.ForeignKey(PrimaryElementOPK)
