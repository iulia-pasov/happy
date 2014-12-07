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
    pub_date = models.DateTimeField('Date', auto_now_add=True)
    privacy = models.CharField(
        max_length=50,
        choices=message_choices,
        default=PUBLIC)
    author = models.ForeignKey(User, related_name='messages')
    messages = models.Manager()

    def __unicode__(self):
        return u'{0}.. by {1}'.format(self.message_content[:4], self.author)
