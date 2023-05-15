from django.db import models
from accounts.models import User
# Create your models here.

class Agents(models.Model):
    agent_img = models.ImageField(upload_to='agents/')
    agent_name = models.CharField(max_length=100)
    agent_desc = models.TextField(max_length=300)
    agent_email = models.EmailField(max_length=50)
    agent_phn_no = models.CharField(max_length=12)

class Blog(models.Model):
    blog_img = models.ImageField(upload_to='blog/')
    blog_name = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    blog_desc = models.TextField()

    class Meta:
        ordering = ['-posted_on']

class About(models.Model):
    image = models.ImageField(upload_to='company/')
    business_background = models.TextField()
    company_profile = models.TextField()

    def summary(request,company_profile):
        return company_profile[:50]

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
    
