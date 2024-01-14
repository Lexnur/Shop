from django.shortcuts import render
from django.http import HttpResponse


def info(request):
    return HttpResponse('Hello! \n Yuo are best!!!')
