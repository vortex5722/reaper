from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')