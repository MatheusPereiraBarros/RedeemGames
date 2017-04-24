from django.db import models
from django.utils import timezone

'''Gerencia os jogos a serem distribuidos no site'''

class Jogo(models.Model):
	idJogo = models.AutoField(primary_key=True)
	nomeJogo = models.CharField(max_length=20)
	descricaoJogo = models.CharField(max_length=500, default='DESCRIÇÃO')
	imagemJogo = models.URLField(max_length=200)
	distribuidora = models.CharField(max_length=50)
	precoJogo = models.BigIntegerField()
	plataformaJogo = models.CharField(max_length=50)


	def publish(self):
		self.save()

	def jogo_id(self):
		return self.id

	def __str__(self):
		return self.nomeJogo

class JogoChave(models.Model):
	idJogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
	chaveAcesso = models.CharField(max_length=100)
	linkDownload = models.URLField(max_length=200, default='www.example.com.br')

	def quantJogos(self):
		return self.objects.count()

	def publish(self):
		self.save()

	def __str__(self):
		return 'Jogo: {0}, Chave: {1}'.format(self.idJogo, self.chaveAcesso)


class Pergunta(models.Model):
	idPergunta = models.AutoField(primary_key=True)
	Pergunta = models.CharField(max_length=200)
	Resposta = models.CharField(max_length=200)
		
	def publish(self):
		self.save()

	def __str__(self):
		return 'Pergunta: {0}'.format(self.Pergunta)

class PostGameSite(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
