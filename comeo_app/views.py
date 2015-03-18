from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {'key': 'value for template'};
    return render(request, 'comeo_app/index.html', context)