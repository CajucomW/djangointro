import os
import glob
import requests
from jinja2 import Template
from django.shortcuts import render

def index(request):
    print("---Processing Index page---")
    context = {}
    return render(request, 'index.html', context)

def tech(request):
    print("---Processing Tech page---")
    context = {}
    return render(request, 'tech.html', context)

def repos(request):
    print("---Processing Repos page---")
    response = requests.get('https://api.github.com/users/cajucomw/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'repos.html', context)

def pta(request):
    print("---Processing PTA page---")
    context = {}
    return render(request, 'pta.html', context)
    
def jiujitsu(request):
    print("---Processing Jiujitsu page---")
    context = {}
    return render(request, 'jiujitsu.html', context)