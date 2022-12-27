from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.models import User

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


# Create your views here.

# class CustomAuthToken(ObtainAuthToken):
#     """
#     Custom export user token
#     """
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         # create token
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key
#         })


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                if created:
                    return Response({
                        'token':token.key,
                        'message':'token created'
                    })
                # else:
                #     token.delete()
                #     token = Token.objects.create(user = user)
                #     return Response({
                #         'token':token.key,
                #         'message': 'token created'
                #     })
            else:
                print('user not activate') 
                return Response({'error':'User not activate'})
        else: 
            print('not valid')
            return Response({'error':'username or password invalid'})
        return Response({'message':'menssage from response'})



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['username', 'email']
    ordering_fields = ['username']
    search_fields = ['username', 'first_name', 'last_name']
    

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['title', 'user', 'tags']
    ordering_fields = ['title']
    search_fields = ['title']


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['content_type', 'description']
    ordering_fields = ['content_type']
    search_field = ['description']


class TypeOfFileViewset(viewsets.ModelViewSet):
    queryset = TypeOfFile.objects.all()
    serializer_class = TypeOfFileSerializer


class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['name', 'user', 'type_of_file']
    ordering_fields = ['name']
    search_fields = ['name']
  