import graphene
from graphene_django import DjangoObjectType

from  .models import *



"""Todo CRUD"""
class CategoryType(DjangoObjectType):
    class Meta:
        model = category

class Todo_type(DjangoObjectType):
    class Meta:
        model = Todo

class TodoInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    Description = graphene.String()
    # category = graphene.ID()
    status = graphene.Boolean(required=True)
 
class CreateTodo(graphene.Mutation):
    todo = graphene.Field(Todo_type)

    class Arguments:
        input = TodoInput(required=True)

    def mutate(self, info, input):
        todo = Todo(
            title=input.title,
            Description=input.Description,
            # category=Category.objects.get(id=input.category),
            status=input.status,
        )
        todo.save()
        return CreateTodo(todo=todo)

class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(Todo_type)

    class Arguments:
        id = graphene.Int(required=True)
        input = TodoInput(required=True)

    def mutate(self, info, id, input):
        todo = Todo.objects.get(id=id)
        todo.title = input.title
        todo.Description = input.Description
        # todo.category = Category.objects.get(id=input.category)
        todo.save()
        return UpdateTodo(todo=todo)

class DeleteTodo(graphene.Mutation):
    todo = graphene.Field(Todo_type)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return DeleteTodo(todo=todo)

class Query(graphene.ObjectType):
    todos = graphene.List(Todo_type)
    category = graphene.List(CategoryType)
    todo = graphene.Field(Todo_type, id=graphene.Int())
    def resolve_todo(self, info, id):
        return Todo.objects.get(id=id)
    def resolve_todos(self, info):
        return Todo.objects.all()

    def resolve_category(self, info):
        return category.objects.all()

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

