from django.contrib import admin
from .models import Article , Articlo , NewModels , Signup

# Register your models here.
#first way to register a model

#admin.site.register(Article)

#second way to register a model
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title' , 'description')
    list_display = ('title' , 'description')

admin.site.register(Articlo)

@admin.register(NewModels)
class NewModel(admin.ModelAdmin):
    list_filter = ('UID','Doctor','gender_choice')
    list_display = ('UID','Doctor','gender_choice')


@admin.register(Signup)
class Signup(admin.ModelAdmin):
    list_filter = ('name','email','mobile','pwd')
    list_display = ('name', 'email', 'mobile', 'pwd')



