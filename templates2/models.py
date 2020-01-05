from django.db import models


class Characters(models.Model):

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/game', null=True,blank=True)


    def __str__(self):
        return self.name