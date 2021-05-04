from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
  return render(request, 'facebook/login.html')

@login_required
def home(request):
  return render(request, 'facebook/home.html')