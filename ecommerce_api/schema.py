import graphene

from user_controller.schema import schema as user_schema


class Query(user_schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)