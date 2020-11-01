from django.db import models

# Create your models here.
class call(models.Model):
    state = models.CharField(max_length=20,default="대기중")
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    gender_filter = models.CharField(max_length=30,default="anybody") #man,woman,anybody
    address = models.CharField(max_length=200,null=True,blank=True)