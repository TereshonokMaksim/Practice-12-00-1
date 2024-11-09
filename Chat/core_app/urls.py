from django.urls import path
from .views import show_core_app

urlpatterns = [
    path('', show_core_app, name = 'core')
]