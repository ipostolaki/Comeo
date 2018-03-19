from django.shortcuts import render, redirect


def home(request):
    return redirect('events:tico_landing')


def future(request):
    return render(request, 'base/future.html')
