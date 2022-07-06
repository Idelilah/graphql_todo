from django.contrib import admin
from .models import *
from django.apps import apps

# Register your models here.

admin.site.register(Todo)
admin.site.register(category)
admin.site.register(User)

app = apps.get_app_config('graphql_auth')

for model, model_item in app.models.items():
    admin.site.register(model_item)