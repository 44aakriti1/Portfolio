
from django.db import models

# This model stores your manual projects (the ones you upload yourself)
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/') # Stores images in a folder
    tech_stack = models.CharField(max_length=200, help_text="Example: Django, React, Python")
    link = models.URLField(blank=True) # Link to live site or code

    def __str__(self):
        return self.title

# This model stores your skills (like Python, Java, etc.)
class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=80) # To show a progress bar

    def __str__(self):
        return self.name