from django.shortcuts import render
from .models import Jogo

def post_list(request):
	jogo = Jogo.objects.all()
	return render(request, 'RedeemGamesWEB/post_list.html', {'usuario': jogo})

# Create your views here.
