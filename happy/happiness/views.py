from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response

from rest_framework import viewsets

from happiness.models import Message
from happiness.serializers import MessageSerializer, UserSerializer


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A view for all the messages
    """
    queryset = Message.messages.all()
    serializer_class = MessageSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A view for all the users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
