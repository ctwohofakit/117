from django.contrib import admin
from .models import Status, Tag


# Register your models here.
from .models import Project
admin.site.register(Project)
admin.site.register(Status)
admin.site.register(Tag)



