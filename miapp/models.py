# mi_aplicacion/models.py
from django.db import models

class Career(models.Model):
    idcareer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=20)
    image = models.ImageField(upload_to='careers/', null=True, blank=True) # Usa ImageField para las imágenes
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# models.py
from django.db import models

class Course(models.Model):
    idcourse = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    hour = models.IntegerField()
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name