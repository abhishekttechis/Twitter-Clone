
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Tweet(models.Model):
    class Meta(object):
        db_table = 'tweets'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=24, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=148, db_index=True
    )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True

    )
    likes = models.PositiveIntegerField(
        'like', default=0, blank=True, db_index=True, null=True
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True
    )
