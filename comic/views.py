from django.shortcuts import render
from user_agents import parse
import urllib.parse



# Create your views here.

def index(request):
    # Aquí va la lógica de tu vista
    return render(request, 'home/index.html')

def index(request):
    apk_url = 'https://github.com/CarolPadilla/APK/raw/main/comics.apk'
    
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(user_agent_string)
    is_mobile = user_agent.is_mobile
    
    return render(request, 'home/index.html', {
        'apk_url': apk_url,
        'is_mobile': is_mobile
    })