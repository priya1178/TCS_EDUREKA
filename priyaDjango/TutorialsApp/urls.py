from django.contrib import admin
from django.urls import path
from TutorialsApp import views

urlpatterns = [
    path('',views.index,name='TutorialsApp'),
    #Lpath('',views.about,name='TutorialsApp'),
    path('contact',views.contact,name='TutorialsApp'),
]