from django.shortcuts import render

# Create your views here.

def index(request):
    # Aquí va la lógica de tu vista
    return render(request, 'home/index.html')