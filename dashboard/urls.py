from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog/<slug:slug>', views.post),
    path('category/<slug:slug>', views.category)
]

handler404 = views.notfound