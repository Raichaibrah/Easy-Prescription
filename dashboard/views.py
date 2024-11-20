from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from pharmacies.models import Pharmacie


# Create your views here.

def index(request):
    pharmacie = Pharmacie.objects.all()
    return render(request, 'dashboard/index.html', context = {"pharmacies" : pharmacie})

def pharmacie_detail(request, slug):
    pharmacie = get_object_or_404(Pharmacie, slug=slug)
    print("pharmacie : ",pharmacie.thumbnail)
    return render(request, 'dashboard/detail.html', context={"pharmacie": pharmacie})
