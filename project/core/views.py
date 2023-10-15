from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, "D:/Manish/Donda/donda/project/core/templates/core/index.html")

