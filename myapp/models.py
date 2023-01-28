from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    name = models.CharField(max_length=250)
    about = models.CharField(max_length=500)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return str(self.name)


class Person(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='proj_as_manager')
    asst_manager = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='proj_as_asst_manager')

    def __str__(self):
        return str(self.name)


class PersonImage(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.FileField(upload_to='person_image/')
    image_info = models.CharField(max_length=200, null=True, blank=True, default="image")
