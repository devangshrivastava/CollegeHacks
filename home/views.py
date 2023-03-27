from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    context = {
        'variable1': "this is sent",
        'variable2': "no this hasn't been sent"
    }
    return render(request, 'index.html', context)

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
def signup(request):
    # return HttpResponse("this is services us page")
    return render(request, 'signup.html')