from django.urls import path,include
from .views import ArticleViews,ArticloViews,NewModelViews
from rest_framework.routers import DefaultRouter
#article_list , article_details

router = DefaultRouter()
router.register('articles',ArticleViews,basename='articles')
router.register('articlo',ArticloViews,basename='articlo')
router.register('Newmodels',NewModelViews,basename='Newmodels')

urlpatterns = [
    path('',include(router.urls)),


    #path('articles/', Articlelist.as_view()),
    #path('articles/<int:id>/', ArticleDetails.as_view()),'''

    #path('articles/', article_list),
    #path('articles/<int:pk>/', article_details),'''
]
