from django.shortcuts import render
from django.utils import timezone
from .models import Jogo
from .models import JogoChave

def jogo(request):
	jogo = Jogo.objects.all()
	#jogochave = JogoChave.objects.all()
	#lista = zip(jogo, jogochave)
	return render(request, 'RedeemGamesWEB/post_list.html', {'jogo': jogo})

'''def jogochave(request):
	jogochave = JogoChave.objects.all()
	return render(request, 'RedeemGamesWEB/post_list.html', {'jogochave': jogochave})

def post_list(request):
	post = PostGameSite.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	jogos = Jogo.objects.all()
	return render(request, 'RedeemGamesWEB/post_list.html', {'jogos': jogos})'''
# Create your views here.
