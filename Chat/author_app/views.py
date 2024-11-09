from django.shortcuts import render

def render_ukr_author(request):
    return render(request = request, template_name = "author_app/ukr_author.html")

def render_zar_author(request):
    return render(request = request, template_name = "author_app/zar_author.html")