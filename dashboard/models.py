from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class module(models.Model):
    
    module = models.CharField(max_length=50)
    tp = models.FloatField(blank=True,null=True)
    td = models.FloatField(null=True)
    exam = models.FloatField(null=True)

    def __str__(self):
        return self.module
    
    def moyen(self)->float:
        if self.tp is None:
            return (self.exam*0.6)+(self.td*0.4)
        else:
            return (self.exam*0.6)+((self.td*0.2)+(self.tp*0.2))
        

class student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,null=True)
    study_year = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=355,null=True)
    modules = models.ManyToManyField(module)

    def __str__(self):
        return self.name

class prof(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=444)
    last_name = models.CharField(max_length=444)
    email = models.EmailField(max_length=254)
    module = models.ForeignKey(module,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.first_name
    