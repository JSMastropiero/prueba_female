from rest_framework.pagination import LimitOffsetPagination

class ArticlePagination(LimitOffsetPagination):
    default_limit = 6
    

class CommentPagination(LimitOffsetPagination):
    default_limit = 4
    

class FilePagination(LimitOffsetPagination):
    default_limit = 2
