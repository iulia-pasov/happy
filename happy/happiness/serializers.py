from django.contrib.auth.models import User

from rest_framework import serializers

from happiness.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    '''Simple message serializer
    '''
    def to_representation(self, instance):
        data = super(MessageSerializer, self).to_representation(instance)
        if data['privacy'] == 'prv':
            data['author'] = 'anonymous'
        else: 
            data['author'] = {'username': data['author']['username'],
                'email': data['author']['email']}
        return data
        
    class Meta:
        model = Message
        fields = ('author', 'pub_date', 'privacy', 'message_content')
        depth = 2

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''Simple message serializer
    '''
    class Meta:
        model = User
        fields = ('username', 'email')

