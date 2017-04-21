from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nomeUsuario = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.nomeUsuario

class Jogo(models.Model):
	idJogo = models.AutoField(primary_key=True)
	nomeJogo = models.CharField(max_length=20)
	imagemJogo = models.URLField(max_length=200)
	distribuidora = models.CharField(max_length=50)
	precoJogo = models.BigIntegerField()
	plataformaJogo = models.CharField(max_length=50)
	chaveAcesso = models.CharField(max_length=100)

	def publish(self):
		self.save()

	def __str__(self):
		return self.nomeJogo

class BancoMoedasUsuario(models.Model):
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	saldoMoedas = models.BigIntegerField()

	def __str__(self):
		return self.saldoMoedas

class Pedido(models.Model):
	idPedido = models.AutoField(primary_key=True)
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	idJogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
	dataPedido = models.DateTimeField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

		def __str__(self):
			return self.title
		
# Create your models here.
