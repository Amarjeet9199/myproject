from unicodedata import name
from django.db import models

# Create your models here.

# todo/todo_api/models.py
from django.db import models
from django.contrib.auth.models import User

class Myapp(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length = 180)
    lastname = models.CharField(max_length = 180)
    companyname = models.CharField(max_length = 180)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip = models.CharField(max_length=10)
    mail = models.EmailField(max_length=30)
    web = models.URLField(max_length=200)
    age = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.firstname