from django.contrib import admin
from task.models import Task
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class taskOption(admin.ModelAdmin):
    
    list_display=("name","status","priority","due_date")
    list_filter=("status","priority")
    search_fields=("name","desc")

admin.site.register(Task,taskOption)
admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.unregister(Group)
    