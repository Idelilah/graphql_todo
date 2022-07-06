import graphene
import authentication.schema as auth_schema
import ToDo.schema as todo_schema

class Query(auth_schema.query, todo_schema.Query, graphene.ObjectType):
    pass

class mutation(auth_schema.mutations, todo_schema.Mutation, graphene.ObjectType):
    pass