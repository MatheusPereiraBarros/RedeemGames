from django.contrib import admin
from .models import Usuario
from .models import Jogo
from .models import BancoMoedasUsuario
from .models import Pedido

admin.site.register(Usuario)
admin.site.register(Jogo)
admin.site.register(BancoMoedasUsuario)
admin.site.register(Pedido)


# Register your models here.
