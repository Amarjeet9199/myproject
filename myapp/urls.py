# todo/todo_api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
from .views import (
    MyappListApiView
)

urlpatterns = [
    path('', MyappListApiView.as_view()),
]