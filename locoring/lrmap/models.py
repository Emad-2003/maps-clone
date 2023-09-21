from django.db import models

# Create your models here.

class mapuser(models.Model):
    username=models.CharField(max_length=50,null=False,unique=True)
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=False)
    password2=models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return "%s %s %s %s" %(self.username,self.first_name, self.last_name, self.email )