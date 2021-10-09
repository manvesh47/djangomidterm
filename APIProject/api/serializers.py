from rest_framework import serializers
from .models import Article,Articlo,NewModels

#creating our serializer class and importing our model class from .models
#here we are using modelserializers
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','description']

class Articleserial(serializers.ModelSerializer):
    class Meta:
        model = Articlo
        fields=['id','name']

class NewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewModels
        fields = ['id','UID','Doctor','gender_choice']

