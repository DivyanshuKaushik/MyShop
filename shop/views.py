# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact,Feedback,Login
from math import ceil
# Create your views here.



def home(request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    #nslides = int(n//4 + ceil((n/4)-(n//4)))
    #dict={'no_of_slides':nslides,'range': range(1,nslides),'product':products}

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = int(n // 4 + ceil((n / 4) - (n // 4)))
        allProds.append([prod, range(1, nSlides), nSlides])


    dict = {'allProds': allProds}

    return render(request, 'shop/home.html', dict)

def productview(request):
    # Fetch the product using the id
    #myid = Product.objects.values('id')
    myid=5
    product = Product.objects.filter(id=myid)
    d={'product': product[0]}

    return render(request,'shop/productview.html',d)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email','')
        password=request.POST.get('password','')
        user = Login(email=email, password=password)
        user.save()
    return render(request, 'shop/signin.html')


def tracker(request):
    return render(request, 'shop/tracker.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email =request.POST.get('email','')
        phone=request.POST.get('phone','')
        feedback=request.POST.get('feedback','')
        hyy = Feedback(name=name, email=email, phone=phone, feedback=feedback)
        hyy.save()
    return render(request, 'shop/feedback.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = int(n // 4 + ceil((n / 4) - (n // 4)))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    dict = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        dict = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', dict)