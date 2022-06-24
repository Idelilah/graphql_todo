from django.urls import path
from ToDo.schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path("api",GraphQLView.as_view(graphiql=True,schema=schema ))
]
