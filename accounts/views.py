from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'accounts/index.html')

@login_required
def home(request):
    return render(request,'accounts/home.html')