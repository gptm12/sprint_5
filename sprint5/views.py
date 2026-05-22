from django.shortcuts import render
from sprint5.models import Posto

# Create your views here.
def home(request):
    postos = Posto.objects.all()
    return render(request, 'home.html', {'postos': postos})
    return render(request, 'detalhes_do_posto.html')