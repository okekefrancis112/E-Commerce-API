import graphene
from .models import User
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):

    class Meta:
        model = User


class RegisterUser(graphene.Mutation):
    status = graphene.Boolean(required=True)
    message = graphene.String(required=True)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, password):
        User.objects.create_user(email, password)

        return RegisterUser(
            status=True,
            message="User created successfully"
        )


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    resolve_users(self, info, **kwargs):
        return User.objects.all()


schema = graphene.Schema(query=Query)