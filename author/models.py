from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name