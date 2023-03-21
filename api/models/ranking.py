from django.db import models
from django.contrib.auth.models import User

class Ranking(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    preguntas_acertadas = models.IntegerField()
    tiempo = models.CharField(max_length=10)
    fecha = models.DateTimeField(auto_now_add=True)
    semana = models.IntegerField(default=1)

    def __str__(self):
        return self.usuario.nombres + ' ' + self.usuario.apellidos + ' - ' + str(self.puntaje)