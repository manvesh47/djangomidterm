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
    name = models.TextField(max_length=50,default='none')
    experience = models.TextField(max_length=50,default='none')

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

class Signup(models.Model):
    name = models.CharField(max_length=20)
    email = models.TextField()
    mobile = models.TextField()
    pwd = models.TextField()

    def __str__(self):
        return self.name

class AdoptPet(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=2)
    breed = models.CharField(max_length=30)
    description = models.CharField(max_length=100)



class Pharmacy(models.Model):
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=40)




