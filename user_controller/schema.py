import graphene
from .models import User
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):

    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    resolve_users(self, info, **kwargs):
        return User.objects.all()


schema = graphene.Schema(query=Query)