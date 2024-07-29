from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.TextField(null=True,blank=True)
    created_at = models.DateField(null=True,blank=True)
    
    is_completed = models.BooleanField(default=False)
    
    
    
class profile(models.Model):
    title = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="profile_pic/")