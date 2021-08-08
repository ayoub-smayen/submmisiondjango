from django.contrib import admin

from . import models

myModels = [models.Post,models.Comment1]  # iterable list
admin.site.register(myModels)

