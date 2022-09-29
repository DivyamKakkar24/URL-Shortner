from django.contrib import admin
from django.urls import path
from shorturl import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("create", views.create, name = 'create'),
    path("<str:s>", views.go, name = 'go')
]