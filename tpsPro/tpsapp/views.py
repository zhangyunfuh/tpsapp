from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')


def sign(request):
    return render(request,'signIn_Register.html')