from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Relationship(models.Model):
    relationship_type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Spouse(models.Model):
    name = models.CharField(max_length=100)
    relation = models.ForeignKey(Relationship, on_delete=models.CASCADE)

