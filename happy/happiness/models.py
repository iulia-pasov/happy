from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    '''Message class
    '''
    PUBLIC = 'pub'
    PRIVATE = 'prv'
    message_choices = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )
    message_content = models.TextField()
    pub_date = models.DateTimeField('Date')
    privacy = models.CharField(
        max_length=50,
        choices=message_choices,
        default=PUBLIC)
    author = models.ForeignKey(User, related_name='messages')
