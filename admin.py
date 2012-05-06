from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from mini.models import PrimaryElementMTM,SonOfPrimaryMTM,PrimaryElementOPK,SonOfPrimaryOPK

from mini.models import UserProfile

admin.autodiscover()
##TODO Create a new user form, free access.... send email, etc...  
###TODO Filter using hasrights to add owner to models
class UserProfileInline(admin.TabularInline):
	model = UserProfile

#define defaul group name
##perhaps in a model... outofthebox....
DEFAULT_GROUP = 'HasRights'
class UserAdmin(admin.ModelAdmin):
	#add profile information for admin
	inlines = [UserProfileInline,]
	##TODO Pending get all the fieldsets for root use.
	#originalfieldset = UserAdmin.get_fieldsets
	#Limit view to show only personal related info for users except for superuser
	def change_view(self,request,object_id):
		try:
			#if you are admin, you can do what you want.
			if request.user.is_superuser:
				self.fieldsets = (
                                                   ('Eres root',{'fields':''}),
#                                                   ('Eres root',{'fields':originalfieldset}),
                                        )


			else:
				if DEFAULT_GROUP in request.user.groups.values_list('name',flat=True):
				#any other with right group, will see next fields
					self.fieldsets = (
					   (None,{'fields':('username','first_name','last_name','email')}),
					)
			#perhaps you can login, but you can modify your data
				else:
					self.fieldsets = (
                        	                   (None,{'fields':('')}),
                                        )


			return super(UserAdmin,self).change_view(request,object_id)
		except:
			#shall not pass
			pass

##return only own information if you are staff.. TODO include, hasright
	def queryset(self,request):	
		if request.user.is_superuser:
			qs = super(UserAdmin,self).queryset(request)
		else:
			qs = super(UserAdmin,self).queryset(request)
			qs = qs.filter(Q(is_staff=True) & Q(is_superuser=False) & Q(id=request.user.id))
		
		return qs

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

class AdminPEMTM(admin.ModelAdmin):
	fieldsets = [
	   (None, {'fields':['name_mtm','extra_info_mtm']})
	]

#	fields = ['name_mtm']
admin.site.register(PrimaryElementMTM,AdminPEMTM)

class AdminSonMTM(admin.ModelAdmin):
	fieldsets = [
           (None, {'fields':['name_son_mtm','irrelevant_info_mtm','myfather_MTM']})
        ]
admin.site.register(SonOfPrimaryMTM,AdminSonMTM)


class AdminPEOPK(admin.ModelAdmin):
        fieldsets = [
           (None, {'fields':['name_opk','extra_info_opk']})
        ]

#       fields = ['name_mtm']
admin.site.register(PrimaryElementOPK,AdminPEOPK)

class AdminSonOPK(admin.ModelAdmin):
        fieldsets = [
           (None, {'fields':['name_son_opk','irrelevant_info_opk','myfather_opk']})
        ]
admin.site.register(SonOfPrimaryOPK,AdminSonOPK)

