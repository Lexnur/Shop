from django.shortcuts import render
from django.http import HttpResponse


def info(request):
    return HttpResponse("Hello! If you reading this - don't worry, "
                        "this sait is under development and adding information")
