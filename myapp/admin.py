from django.contrib import admin
from . import models


admin.site.register(models.Publisher)
admin.site.register(models.Book)

admin.site.register(models.Person)
admin.site.register(models.Project)
admin.site.register(models.PersonImage)
