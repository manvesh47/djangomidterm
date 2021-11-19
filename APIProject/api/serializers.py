from rest_framework import serializers
from .models import Article,Articlo,NewModels,Signup,AdoptPet,Pharmacy

#creating our serializer class and importing our model class from .models
#here we are using modelserializers
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','description','name','experience']

class Articleserial(serializers.ModelSerializer):
    class Meta:
        model = Articlo
        fields=['id','name']

class NewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewModels
        fields = ['id','UID','Doctor','gender_choice']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['id','name','email','mobile','pwd']

class AdoptPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptPet
        fields = ['id','name','age','breed','description']

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id','name','contact','description','location']



