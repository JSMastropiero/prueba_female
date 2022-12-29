from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter


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
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('username', 'first_name', 'last_name')

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title','description', 'tags', 'user__username', 'user__first_name', 'user__last_name')


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('description', 'content_type__article')


class TypeOfFileViewset(viewsets.ModelViewSet):
    queryset = TypeOfFile.objects.all()
    serializer_class = TypeOfFileSerializer


class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description', 'user__username', 'user__first_name', 'user__lastname')

