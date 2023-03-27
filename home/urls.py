from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("Maths_1", views.Maths_1, name='Maths_1'),
    path("signup", views.signup, name='signup'),
]