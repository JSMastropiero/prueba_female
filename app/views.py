from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

# Create your views here.

class CustomAuthToken(ObtainAuthToken):
    """
    Custom export user token
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # create token
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })


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