from django.urls import path
from .views import render_ukr_author, render_zar_author

urlpatterns = [
    path("ukr/",render_ukr_author, name = "ukr_author"),
    path("zar/",render_zar_author, name = "zar_author")
]