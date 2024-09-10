from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Freia Arianti Zulaika',
        'kelas' : 'PBP C',
    }

    return render(request, "main.html", context)