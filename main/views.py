from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Freia Arianti Zulaika',
        'npm' : '2306152254',
    }

    return render(request, "main.html", context)