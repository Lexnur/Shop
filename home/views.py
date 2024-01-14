from django.shortcuts import render
from django.http import HttpResponse


def info(request):
    return HttpResponse('Hello! Yuo are best!!!')
