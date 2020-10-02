#my file
from django.shortcuts import render
def index1(request):
    return render(request, 'page.html')

def first(request):
    return render(request, 'page.html')
