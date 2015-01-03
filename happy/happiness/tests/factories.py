import factory

from happiness.models import Message

from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    ''' User Factory '''
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'test'

class MessageFactory(factory.DjangoModelFactory):
    ''' Message Factory '''
    FACTORY_FOR = Message

    author = factory.SubFactory(UserFactory)
