from django.conf.urls import url

#from django.urls import path

from . import views

urlpatterns = [
    url(r'home',views.home),
    url(r"products/", views.productview, name="products"),
    url(r'checkout/', views.checkout, name="checkout"),
    url(r'search/', views.search),
    url(r'about', views.about),
    url(r'contact', views.contact),
    url(r'tracker', views.tracker),
    url(r'feedback', views.feedback),
    url(r'login', views.login)


]

