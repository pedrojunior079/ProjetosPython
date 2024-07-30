import datetime
from django.db import models
from django.utils import timezone


class Pergunta(models.Model):
    pergunta_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data de publicação")

    def __str__(self):
        return self.pergunta_text
    
    def was_published_recentl(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    escolha_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.escolha_text