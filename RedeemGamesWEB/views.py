from django.shortcuts import render
from .models import Usuario

def post_list(request):
	usuario = Usuario.objects.all()
	return render(request, 'RedeemGamesWEB/post_list.html', {'usuario': usuario})

# Create your views here.
