from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message_content = models.TextField()
    pub_date = models.DateTimeField('Date')
    privacy = models.CharField(max_length=50)
    author = models.ForeignKey(User)
