from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name



class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform ,on_delete=models.CASCADE,related_name = 'watchlist')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    ratting = models.PositiveIntegerField(validators =[MinValueValidator(1),MaxValueValidator(5)])
    desc = models.CharField(max_length=100)
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name = 'reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        string = str(self.ratting)+" "+str(self.watchlist.title)
        return string
