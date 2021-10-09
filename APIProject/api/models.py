from django.db import models


#creating a choice field
gender = (
    ("1","male"),
    ("2","female"),
    ("3","non binary"),
    ("4","Trans"),
)
# Create your models here.
# we are creating a model here
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    #creating a def str to return the title
    def __str__(self):
        return self.title

class Articlo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class NewModels(models.Model):
    UID = models.CharField(max_length=10)
    Doctor = models.BooleanField()
    gender_choice = models.CharField(max_length=20,choices=gender,default='1')