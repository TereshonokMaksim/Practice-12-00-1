from django.urls import path
from .views import render_ukr_book, render_zar_book

urlpatterns = [path('ukr_book/',render_ukr_book, name = "ukr_book"),
               path('zar_book/', render_zar_book, name = "zar_book")
               ]
