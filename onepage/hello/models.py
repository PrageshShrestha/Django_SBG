
from django.db import models

# class Visitors(models.Model):
#     Browser_type = models.CharField(max_length = 100)   
#     Ip = models.IntegerField()    
#     Browser_version = models.CharField(max_length = 100)    
#     OS_type = models.CharField(max_length = 100)    
#     Os_version = models.CharField(max_length = 100)    
 
class Comments(models.Model):
    comments = models.CharField(max_length = 200 , null = True)
    comment_date = models.DateTimeField('%d/%m/%d' , null = True)
    class meta:
        
        db_name = 'comments'
class Login(models.Model):
    login = models.EmailField(null = False)
    password = models.CharField(null=False ,  max_length = 20)
    keep_logged = models.BooleanField(default=False)
    class meta:
        db_name = 'login'        
# Create your models here.
