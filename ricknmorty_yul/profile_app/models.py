from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    planet = models.ForeignKey(Planet, null=True, on_delete=models.SET_NULL)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    species = models.ForeignKey(Species, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    # avatar = models.ImageField(upload_to='posters/', default='posters/no-cover.png')


