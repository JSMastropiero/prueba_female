from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.contrib.auth.models import User



# Create your models here.


class Article(TimeStampedModel, SoftDeletableModel):

    title = models.CharField(
        max_length=50,
        verbose_name=('title')
    )
    description = models.TextField(
        verbose_name=('description'),
        blank=True
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=('user'),
        null=True,
        blank=True        
        
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=('is active')
    )
    tags = models.TextField(
        verbose_name=('tags'),
        blank=True
    )
    
    class Meta():
        verbose_name=('article')
        verbose_name_plural=('articles')

    def __str__(self):
        return self.title


class Comment(TimeStampedModel, SoftDeletableModel):

    content_type = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name=('content type'),
        null=True,
        blank=True

    ) 
    description = models.TextField(
        verbose_name=('description'),
        blank=True
    )
    id_context = models.IntegerField(
        verbose_name=('id context'),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=('is active')
    )

    class Meta():
        verbose_name = ('comment')
        verbose_name_plural = ('comments')
    

    def __str__(self):
        return self.description


class TypeOfFile(models.Model):

    name = models.CharField(
        max_length=50,
    )
    class Meta():
        verbose_name = ('type of file')
        verbose_name_plural = ('type of files')

    def __str__(self):
        return self.name


class File(TimeStampedModel, SoftDeletableModel):
    
    name = models.CharField(
        max_length=50,
        verbose_name=('name')
    )
    description = models.TextField(
        verbose_name=('description'),
        blank=True
    )
    size = models.IntegerField(
        verbose_name=('size'),
        null=True,
        blank=True
        
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        blank=True,
        null=True
    )
    type_of_file = models.ForeignKey(
        TypeOfFile,
        on_delete=models.CASCADE,    
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=('is active')
    )

    class Meta():
        verbose_name = ('file')
        verbose_name_plural = ('files')

    def __str__(self):
        return self.name