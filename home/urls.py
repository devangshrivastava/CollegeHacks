from django.contrib import admin
from django.urls import path
from . import views



app_name = "home"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("Maths_1", views.Maths_1, name='Maths_1'),
    # path("signup", views.signup, name='signup'),
    path("maths_batch_2025", views.maths_batch_2025, name='maths_batch_2025'),
    path("sendfiles",views.send_files,name="sendfiles"),
    path("register",views.registerPage,name="register"),
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("upload",views.upload,name="upload")
]
