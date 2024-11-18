from django.shortcuts import render
from django.http import HttpResponse
from pharmacies import models
from dashboard import das

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')
