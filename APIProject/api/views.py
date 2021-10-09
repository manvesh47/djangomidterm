from django.shortcuts import render , HttpResponse
from .models import Article,Articlo,NewModels
from .serializers import ArticleSerializer,Articleserial,NewModelSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.



#using model view sets
class ArticleViews(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticloViews(viewsets.ModelViewSet):
    queryset = Articlo.objects.all()
    serializer_class = Articleserial

class NewModelViews(viewsets.ModelViewSet):
    queryset = NewModels.objects.all()
    serializer_class = NewModelSerializer





#using generic viewsets
'''class ArticleViews(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


'''


#using viewsets
class ArticleViews(viewsets.ViewSet):
    def list(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles , many=True)

        return Response(serializer.data)

    def create(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)
        return Response(serializer,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Article.objects.all()
        artivle = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(artivle)
        return Response(serializer.data)

    def destroy(self,request,pk=None):
        queryset = Article.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class Articlelist(generics.GenericAPIView , mixins.ListModelMixin ,
                  mixins.CreateModelMixin):
    # we are using mixins rather than simple way of retrieving the data
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)




class ArticleDetails(generics.GenericAPIView , mixins.ListModelMixin ,
                     mixins.UpdateModelMixin , mixins.DestroyModelMixin ,
                     mixins.RetrieveModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'
    def get(self,request,id):
        return self.retrieve(request,id=id)
    def put(self,request,id):
        return self.update(request,id=id)
    def delete(self,request,id):
        return self.destroy(request,id=id)



'''
@api_view(['GET' , 'POST'])
def article_list(request):
    if request.method == 'GET':
        #for getting our values we will use our serializer function
        #which we created for our model and Response
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #if we are passing the data then in that case we will need to
        #just request the data if we are using our apiview along with response framework

        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'PUT' , 'DELETE' ])
def article_details(request,pk):
    try:
        #here we are getting values for a certain id in our model
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        #changing the data for that particular id

        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        #deleting the data for our id
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


'''
