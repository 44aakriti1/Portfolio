
from django.contrib import admin
from .models import Project, Skill

# Registering models so they show up in the admin dashboard
admin.site.register(Project)
admin.site.register(Skill)