from django.contrib import admin

from app import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Tag)
admin.site.register(models.Post)
