from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("search_phone_number", views.search_phone_number, name='search_phone_number'),
    path("login_user", views.login_user, name='login_user'),
    path('change_to_spam', views.change_to_spam, name='change_to_spam')
]
