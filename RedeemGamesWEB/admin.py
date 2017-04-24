from django.contrib import admin
from .models import Jogo
from .models import JogoChave
from .models import Pergunta
from .models import PostGameSite

admin.site.register(Jogo)
admin.site.register(JogoChave)
admin.site.register(Pergunta)
admin.site.register(PostGameSite)

# Register your models here.
