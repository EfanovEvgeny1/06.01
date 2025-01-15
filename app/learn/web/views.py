from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import ArticleSerializer

class ArticleView(ListCreateAPIView): #реализует post and get запросы

    queryset = Article.objects.all() #базовый запрос к базе данных для получения объектов
    serializer_class = ArticleSerializer #Это класс сериализатора, который используется для проверки и десериализации объектов из базы

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

class SingleArticleView(RetrieveUpdateDestroyAPIView):#реализует методы put and patch and delete
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer