from pyexpat import model
from graphene_django.types import DjangoObjectType
from users.models import ExtendUser
from .models import *


class ExtendUserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields=["username","email","first_name","last_name"]

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields='__all__'

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields='__all__'

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields=("name",)


class CommentType(DjangoObjectType):
    class Meta:
        model=Comment
        fields='__all__'
