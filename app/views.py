from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.models import User


# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TypeOfFileViewset(viewsets.ModelViewSet):
    queryset = TypeOfFile.objects.all()
    serializer_class = TypeOfFileSerializer


class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer