from django.contrib import admin
from . import models

# Register your models here.

# will allow you to see and edit 'GroupMember' with parent class 'Group' in admin of site
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)


