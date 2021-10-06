from django.http.response import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse(''' <h1> <a  href="/api">APi</a> </h1>   <h1> <a  href="/admin">Admin</a> </h1> ''')