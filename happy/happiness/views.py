from django.contrib.auth.models import User

from rest_framework import viewsets, generics, permissions

from happiness.models import Message
from happiness.serializers import MessageSerializer, UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    A view for all the messages
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Message.messages.order_by('-pub_date')
    serializer_class = MessageSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A view for all the users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
