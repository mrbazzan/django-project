from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.TextField()


class Comment(models.Model):
    
    # Stores the model type
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    
    # Stores the primary key of the related object
    object_id = models.PositiveIntegerField()
    
    # Links to the actual object
    content_object = GenericForeignKey('content_type', 'object_id')
    
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.content_type} with ID {self.object_id}"

