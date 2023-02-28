from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    tags = models.CharField(max_length=500) #To store a List of strings that have been converted into JSON
    content = models.CharField(max_length=500) # Dictionary Bullet point string, status string
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)