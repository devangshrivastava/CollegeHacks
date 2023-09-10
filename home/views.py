from django.shortcuts import render, HttpResponse, redirect
from .models import FilesAdmin
import os
from django.conf import settings
from .models import myuploadfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import CreateUserForm,UploadAllFiles
from django.contrib import messages
from .decorator import allowed_users
from django.contrib.auth.models import User
# from .filters import OrderFilter


@login_required(login_url ='/login')
def index(request):
    # return HttpResponse("this is homepage")
    # files = myuploadfile.objects.all()
    # myFilter = OrderFilter(request.GET, queryset=files)
    # files = myFilter.qs
    # context = {
    #     'myFilter':myFilter
    # }
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("this is about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("this is contact us page")
    return render(request, 'contact.html')

def services(request):
    # return HttpResponse("this is services us page")
    return render(request, 'services.html')

def Maths_1(request):
    # return HttpResponse("this is services us page")
    return render(request, 'maths_1.html')


def maths_batch_2025(request):
    context = {'tutorials' : myuploadfile.objects.filter(course = "Mathematics-1", type = "Tutorials"),
               'quiz' : myuploadfile.objects.filter(course = "Mathematics-1", type = "Quiz"),
               'major_minor' : myuploadfile.objects.filter(course = "Mathematics-1", type = "Major/Minor")
               }
    print(context['tutorials'][0].f_name)
    return render(request, 'maths_batch_2025.html' ,context)

@login_required(login_url ='/login/')
def home(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request,'')


def send_files(request):
    # import pdb;
    # pdb.set_trace()
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfiles")
        file_dir = request.POST.get("file_getdir")
        for f in myfile:
            myuploadfile(f_name=name,myfiles=f).save()
        return HttpResponse("ok")

@allowed_users(allowed_roles = ['Teachers'])
def upload(request):
    # import pdb
    # pdb.set_trace()
    form = UploadAllFiles()
    if request.method == 'POST':
        f_name = request.POST.get("f_name")
        myfiles = request.FILES.get("myfiles")
        course = request.POST.get("course")
        batch = request.POST.get('batch')
        type = request.POST.get('type')
        # for f in myfiles:
        myuploadfile(f_name=f_name,myfiles=myfiles,course=course,batch=batch,type=type).save()
        messages.success(request, f_name + ' was uploaded! ')
    context = {'form':form}
    return render(request, 'upload.html',context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/') 
    else:
        # if(request.user.email.split('@')[1] ==  == "iitj.ac.in"):
        form = CreateUserForm(request.POST)
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            print(request.POST.get('password1'))
            print(request.POST.get('password2'))
            if form.is_valid() and request.POST.get('email').split('@')[1] == "iitj.ac.in":
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Accounts was created for ' +user)
                return redirect('/login')
            elif(request.POST.get('email').split('@')[1] != "iitj.ac.in"):
                messages.info(request, 'not a user from iitj')
            elif User.objects.filter(username=request.POST.get('username')).exists():
                messages.info(request, 'username already exist!')
            else:
                messages.info(request, 'username or password incorrect, try some other combinations!!')

            # return HttpResponse("unsuccessful")
            # messages.success(request, 'unsuccessful')
            # return redirect('/register')
        context = {'form':form}
        return render(request, 'Register.html',context)
        

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/') 
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username =username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
            
            else:
                messages.info(request, 'Username or the Password is INCORRECT')

        return render(request, 'login.html')

def logoutUser(request):
    print(1)
    logout(request)
    print(2)
    return redirect('home:login')