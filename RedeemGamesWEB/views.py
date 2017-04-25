from django.shortcuts import render
from django.utils import timezone
from .models import Jogo
from .models import PostGameSite

def jogo(request):
	jogo = Jogo.objects.all()
	return render(request, 'RedeemGamesWEB/post_list.html', {'game': jogo})

def post(request):
	post = PostGameSite.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'RedeemGamesWEB/post_list.html', {'postagem': post})
# Create your views here.
