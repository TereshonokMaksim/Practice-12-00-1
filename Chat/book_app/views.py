from django.shortcuts import render

# Create your views here.
def render_ukr_book(request):
    return render(request = request, template_name = "book_app/ukr_book.html")

def render_zar_book(request):
    return render(request = request, template_name = "book_app/zar_book.html")