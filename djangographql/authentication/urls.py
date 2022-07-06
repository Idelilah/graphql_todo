from django.urls import path
from authentication.schema import schema
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("",csrf_exempt(GraphQLView.as_view(graphiql=True,schema=schema )))
]
