from django.shortcuts import render


def home(request):
    return render(request, 'base/index.html')


def faq(request):
    return render(request, 'base/faq.html')


def about(request):
    return render(request, 'base/about.html')


def ro(request):
    # romanian language localization mock page showing "translation in progress" text
    return render(request, 'base/ro.html')
