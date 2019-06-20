from django.db import models

from django.urls import reverse

class Docente(models.Model):
    foto = models.ImageField(upload_to='static/media/',default = 'static/media/no-img.png',null=True, blank=True)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    edad =models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('docente_detail',kwargs={'pk': self.pk})

class Asignatura(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('asignatura_detail', kwargs={'pk': self.pk})

class Grupo(models.Model):
    codigo = models.CharField(max_length=10)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{},{}".format(self.codigo,self.docente,self.asignatura)

    def get_absolute_url(self):
        return reverse('grupo_detail', kwargs={'pk': self.pk})

