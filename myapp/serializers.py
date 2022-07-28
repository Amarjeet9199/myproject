# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Myapp
class MyappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myapp
        fields = ["id", "firstname", "lastname",  "companyname",  "city",  "state",  "zip", "mail", "web", "age", "user"]
