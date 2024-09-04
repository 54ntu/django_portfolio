from django.db import models
from django.contrib.auth import get_user_model


User =get_user_model()

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    

class Portfolio(models.Model):
    image = models.ImageField()


class Comments(models.Model):
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE)
    blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)



class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_url = models.CharField(max_length=150)
    tech_used = models.TextField()