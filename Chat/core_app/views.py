from django.shortcuts import render


def show_core_app(requests):
    return render(request = requests, template_name = "core_app/core.html")
# Create your views here.
