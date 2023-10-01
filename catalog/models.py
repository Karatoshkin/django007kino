from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Director(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.fname},{self.lname}'

class Actor(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    born = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.lname

class Status(models.Model):
    Vibor = (('бесплатно','бесплатно'),('базовая','базовая'),('супер','супер'))
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Country (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class AgeRate(models.Model):
    choise = (('G','G'), ('PG', 'PG'),('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    rate = models.CharField(max_length=20, choices = choise)

    def __str__(self):
        return self.rate

class Film(models.Model):
    title = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=1)
    rating = models.FloatField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500)
    year = models.IntegerField()
    ager = models.ForeignKey(AgeRate, on_delete=models.SET_NULL, null=True)
    actor = models.ManyToManyField(Actor)
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title

    def display_actors(self):
        res=' '
        for a in self.actor.all():
            res+=a.lname+' '
        return res